
# PPPP    Y   Y  TTTTT  H   H   OOO    N   N     
#  P   P    Y Y     T    H   H  O   O   NN  N    
#   PPPP      Y      T    HHHHH  O   O   N N N   
#    P         Y      T    H   H  O   O   N  NN  
#     P         Y      T    H   H   OOO    N   N 

#     P         Y      T    H   H   OOO    N   N 
#    P         Y      T    H   H  O   O   N  NN  
#   PPPP      Y      T    HHHHH  O   O   N N N   
#  P   P    Y Y     T    H   H  O   O   NN  N    
# PPPP    Y   Y  TTTTT  H   H   OOO    N   N     



import re

from typing import List, Set, Tuple

import Levenshtein

import pymorphy2

from .transliteration_map import transliteration_map

from .utils import (
    load_banned_words_with_ratings_from_csv,
    load_words_from_csv_file,
    load_words_from_directory,
)


class TextModeration:
    def __init__(
        self,
        banned_words: List[str],
        hard_banned_words: List[str],
        levenshtein_distance_threshold: int = 2,
    ):
        self.banned_words: Set[str] = set(banned_words)
        self.hard_banned_words: Set[str] = set(hard_banned_words)
        self.morph = pymorphy2.MorphAnalyzer()
        self.transliteration_map = transliteration_map
        self.levenshtein_distance_threshold = levenshtein_distance_threshold

    def clean_text(self, text):

        text = re.sub(r"(?<=\s)[^\w\s]+(?=\s)", " ", text)
        text = re.sub(r"^\W+|\W+$", "", text)  # Убираем знаки в начале и в конце текста
        text = re.sub(r"\s+", " ", text).strip()  # Убираем лишние пробелы между словами
        return text.lower()

    # @lru_cache(maxsize=10000)  # Кэшируем до 10,000 слов # Пока не будем
    def lemmatize_word(self, word):

        return self.morph.parse(word)[0].normal_form

    def extract_and_lemmatize_words(self, text):

        # Используем регулярное выражение для извлечения слов (буквы, цифры, символы подчеркивания)
        words = re.findall(r"\w+", text.lower())
        return [self.lemmatize_word(word) for word in words]

    def transliterate_word_base(self, word: str) -> str:
  
        return translit(word, "ru")

    def transliterate_word(self, word: str) -> List[str]:
        """
        Генерирует все возможные варианты транслитерации слова.

        Args:
            word (str): Слово для транслитерации.

        Returns:
            List[str]: Список всех возможных транслитераций.
        """

        def generate_combinations(current: str, remaining: str) -> List[str]:
            if not remaining:
                return [current]

            char = remaining[0]
            rest = remaining[1:]

            if char in self.transliteration_map:
                options = self.transliteration_map[char]
                combinations = []
                for option in options if isinstance(options, list) else [options]:
                    combinations.extend(generate_combinations(current + option, rest))
                return combinations
            else:
                return generate_combinations(current + char, rest)

        return generate_combinations("", word.lower())

    def transliterate_sentence(self, sentence):

        words = sentence.split()
        results = []

        for word in words:
            if re.search(
                r"[a-zA-Z*@(-01]", word
            ):  # Проверка на латиницу или специальные символы
                transliterated_words = self.transliterate_word(word)
                base_translit = self.transliterate_word_base(word)

                # print("base_translit ",  base_translit)

                transliterated_words.append(base_translit.lower())
                results.extend(transliterated_words)
            else:
                results.append(word)

        return results

    def process_text(self, text):

        text_lower = text.lower()  # Приведение к нижнему регистру
        text_lower = self.clean_text(text_lower)  # Очистка текста

        # Транслитерация текста
        transliterated_texts = set(
            self.transliterate_sentence(text_lower)
        )  # Убираем дубликаты

        # Вариант оптимизации
        # # Объединяем все строки в одну, разделённую пробелами
        # combined_text = ' '.join(transliterated_texts)
        # # Заменяем множество на эту объединённую строку
        # transliterated_texts = {combined_text}

        transliterated_texts.add(text_lower)  # Добавляем оригинальный текст

        # print(transliterated_texts)

        # Лемматизация только оригинального текста
        lemmatized_texts = set(self.extract_and_lemmatize_words(text_lower))

        # print("\n lemmatized_texts   ", lemmatized_texts)

        # Возвращаем объединённое множество лемматизированных и транслитерированных слов
        return lemmatized_texts.union(transliterated_texts)

    def is_near_match(self, word: str, banned_word: str) -> bool:

        return (
            Levenshtein.distance(word, banned_word)
            <= self.levenshtein_distance_threshold
        )

    def _check_word_list(self, text_words: List[str], banned_words: Set[str]) -> bool:

        for banned_word in banned_words:
            if banned_word in text_words:
                return True

            for word in text_words:
                if self.is_near_match(word, banned_word):
                    return True

        return False

    def has_banned_words(
        self, text: str, check_hard_banned, check_banned):

        # Получаем объединённый набор лемматизированных и транслитерированных слов
        all_texts = self.process_text(text)

        # Проверка на наличие запрещённых слов
        if check_banned and self._check_word_list(all_texts, self.banned_words):
            return 0.8, True
        if check_hard_banned and self._check_word_list(
            all_texts, self.hard_banned_words
        ):
            return 1.0, True

        return 0.0, False

    def check_banned_words_with_weights(
        self, text, filename):
        # Загружаем слова и их веса из файла
        banned_words_with_weights = load_banned_words_with_ratings_from_csv(filename)

        # print(banned_words_with_weights)

        # Получаем объединённый набор лемматизированных и транслитерированных слов
        all_texts = self.process_text(text)

        total_weight = 0.0
        found_banned = False

        # Создаём словарь для быстрого доступа к весам и категориям
        banned_dict = {
            item["word"]: (item["category"], item["weight"])
            for item in banned_words_with_weights
        }

        found_words = []

        # Проверяем каждое слово в тексте на наличие в списке запрещённых слов
        for word in all_texts:
            # Проверяем точное совпадение
            if word in banned_dict:
                found_banned = True
                category, weight = banned_dict[word]
                total_weight += weight  # Суммируем вес найденных слов
                found_words.append(word)
                continue  # Переходим к следующему слову

            # Проверяем близость по написанию с учетом расстояния Левенштейна
            for banned_word, (category, weight) in banned_dict.items():
                if self.is_near_match(word, banned_word):
                    found_banned = True
                    total_weight += weight  # Суммируем вес найденных слов
                    found_words.append(banned_word)
                    break  # Выходим из цикла для данного слова

        # Определяем вероятность блокировки текста на основе общего веса
        probability = total_weight  # Примерное преобразование веса в вероятность

        # Проверка: если вероятность больше 1, устанавливаем её равной 1
        if probability > 1:
            probability = 1.0

        # print(found_worlds)

        return probability, found_banned

    def check_banned_words_with_categories(
        self, text: str, banned_words_file: str, categories_file: str
    ) -> Tuple[float, bool]:


        # Загружаем запрещённые слова и их категории из файла
        banned_words_with_weights = load_banned_words_with_ratings_from_csv(
            banned_words_file
        )
        # print("Banned words loaded:", banned_words_with_weights)

        # Загружаем категории и их коэффициенты
        categories_list = load_categories_from_csv(categories_file)
        # print("Categories loaded:", categories_list)

        # Преобразуем список категорий в словарь для быстрого доступа
        categories = {item["category"]: item["coefficient"] for item in categories_list}
        # print("Categories dictionary:", categories)

        # Получаем обработанный текст как список слов
        all_texts = self.process_text(text)
        # print("Processed text:", all_texts)

        total_probability = 0.0
        found_banned = False

        # Создаём словарь для быстрого доступа к категориям запрещённых слов
        banned_dict = {
            item["word"]: item["category"] for item in banned_words_with_weights
        }
        # print("Banned words dictionary:", banned_dict)

        # Проверяем каждое слово в тексте на наличие в списке запрещённых слов
        for word in all_texts:
            # print(f"Checking word: {word}")
            # Проверяем точное совпадение
            if word in banned_dict:
                found_banned = True
                category = banned_dict[word]
                coefficient = categories.get(
                    category
                )  # Получаем коэффициент для категории

                # print(f"Found exact match: {word} (Category: {category}, Coefficient: {coefficient})")

                if coefficient is not None:
                    total_probability += (
                        coefficient  # Суммируем вероятности на основе коэффициентов
                    )

                continue  # Переходим к следующему слову

            # Проверяем близость по написанию с учётом расстояния Левенштейна
            for banned_word in banned_dict.keys():
                if self.is_near_match(word, banned_word):
                    found_banned = True
                    category = banned_dict[banned_word]
                    coefficient = categories.get(
                        category
                    )  # Получаем коэффициент для категории

                    # print(f"Found close match: {banned_word} (Category: {category}, Coefficient: {coefficient})")

                    if coefficient is not None:
                        total_probability += (
                            coefficient  # Суммируем вероятности на основе коэффициентов
                        )

                    break  # Выходим из цикла для данного слова

        # Ограничиваем вероятность до 1.0
        if total_probability > 1:
            total_probability = 1.0

        # print(f"Final Total Probability: {total_probability}, Found Banned Words: {found_banned}")

        return total_probability, found_banned


if __name__ == "__main__":
    # НОВЫЙ ФАИЛ
    banned_words_file = r"D:\Pets\NetTyan\Python\NetTyanRepo\NetTyan\docker\filter\feature_filter\data\block_words\banned_words_cat_2_2.csv" # "banned_words_cat_2_2.csv"

    categories_file = r"D:\Pets\NetTyan\Python\NetTyanRepo\NetTyan\docker\filter\feature_filter\data\block_words\categories_2.csv" # "categories_2.csv"

    text_moderation = TextModeration(
        banned_words=[],
        hard_banned_words=[],
        levenshtein_distance_threshold=0.5  # LEVENSHTEIN_DISTANCE,
    )

    test_cases = [
        ("I like jfdkhwemvsddsfd kfdjfkjdsfasssaqng.", 0.6, True),
        ("I like  президент  пробный текст эксперимент слово.", 0.35, True),
        ("Привет, как дела?", 0.35, False),
        ("Друзья, что случилось?", 0.35, False),
        ("CJlaDКа9л БеПа Давай поговорим о чем то интересном в игре без этих глупостей", 0.9, False),
        ("хуем тя кто подтянул отвечай с члена?", 0.9, False),
        ("Mat_Eby_Tvoy", 0.9, False),
        # ("I like grapes and oranges.", 0.3, True),  #
    ]

    for input_text, expected_probability, expected_found in test_cases:
        probability, has_banned = text_moderation.check_banned_words_with_categories(
            input_text, banned_words_file, categories_file
        )
        print(
            f"Input: {input_text}\nTotal Probability: {probability}, Expected: {expected_probability}, Found Banned Words: {has_banned}, Expected Found: {expected_found}\n"
        )

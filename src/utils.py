# PPPPP    YYYYY    TTTTT    HHHHH     OOOOO    NNNNN
# P    P    YYY       TTT     H   H    O   O    N   N
# PPPPP      Y        TTT     HHHHH    O   O    N   N
# P          Y        TTT     H   H    O   O    N   N
# P          Y        TTT     H   H     OOO     N   N

# ~SNAKE~


import csv
import os


def load_words_from_directory(directory):


    words_list = []  # Список для хранения загруженных слов
    for file_name in os.listdir(directory):
        if file_name.endswith(".csv"):
            file_path = os.path.join(directory, file_name)
            with open(file_path, newline="", encoding="utf-8") as csvfile:
                reader = csv.reader(csvfile)  #
                for row in reader:
                    if row:  # Проверяем, что строка не пустая
                        words_list.append(row[0])  # Добавляем первое значение в строке
    return words_list  # Возвращаем список загруженных слов


def load_words_from_csv_file(filename):

    words_list = []  # Список для хранения загруженных слов
    with open(filename, newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)  # Используем csv.reader для файлов без заголовков
        for row in reader:
            if row:  # Проверяем, что строка не пустая
                words_list.append(row[0])  # Добавляем первое значение в строке
    return words_list  # Возвращаем список загруженных слов


def load_test_samples(filename):


    with open(filename, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        return [(row["text"], row["expected"] == "True") for row in reader]


def load_banned_words_with_ratings_from_csv(filename):

    words_list = []  # Список для хранения загруженных слов
    expected_header = ["word", "category", "weight", "label"]  # Ожидаемый заг

    with open(filename, newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)  # Используем csv.rea
        header = next(reader)  # Читаем первую

        # Проверяем, со
        if header != expected_header:
            raise ValueError(
                f"Некорректный заголовок в файле {filename}. Ожидается: {expected_header}, получено: {header}"
            )

        # Загружаем данные из файла, начиная со второй строки
        for row in reader:
            if (
                row and len(row) >= 4
            ):  # Проверяем, что 
                word_data = {
                    "word": row[0],  # Первое зн
                    "category": row[1],  # Второе зн
                    "weight": float(
                        row[2]
                    ),  # Третье значен
                    "label": row[3],  # Четвертое зн
                }
                words_list.append(word_data)  # Добавляем

    return words_list  # Возвращаем список з

def load_categories_from_csv(filename):

    data = []  # List to store the loaded data

    with open(filename, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)  # Use DictReader to 
        for row in reader:
            # Append each row to the data list
            data.append(
                {
                    "category": row["category"],  # Correct k
                    "coefficient": float(
                        row["coefficient"]
                    ),  # Convert c
                    "label": row["label"],  # Corre
                }
            )

    return data


if __name__ == "__main__":
    input_file = "_categories.csv"  # Specify the path to your CSV file
    loaded_data = load_categories_from_csv(input_file)

    print("Loaded data:")
    for item in loaded_data:
        print(item)


    #     # Пример использования функции
    # filename = 'words.csv'  # Имя вашего CSV-файла
    # ----------------------------------------------------------------
    # try:
    #     banned_words = load_banned_words_with_ratings_from_csv(filename)
    #     print("Запрещённые слова успешно загружены: \n", banned_words)
    # except ValueError as e:
    #     print(e)

    # # Загружаем слова из CSV-файла
    # words = load_banned_words_with_ratings_from_csv(filename)

    # # Вывод загруженных данных
    # for word in words:
    #     print(word)

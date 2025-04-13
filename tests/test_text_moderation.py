import unittest

from src.text_moderation import TextModeration


class TestTextModeration(unittest.TestCase):
    def setUp(self):
        self.banned_words = ["спам", "мошенничество", "фейк"]
        self.hard_banned_words = ["оскорбление", "ругательство"]
        self.levenshtein_distance_threshold = 2
        self.moderation = TextModeration(
            self.banned_words,
            self.hard_banned_words,
            self.levenshtein_distance_threshold,
        )


    def test_lemmatize_word(self):
        word = "играю"
        expected = "играть"
        self.assertEqual(self.moderation.lemmatize_word(word), expected)



    def test_extract_and_lemmatize_words(self):
        text = "Я люблю играть в игры."
        expected = ["я", "любить", "играть", "в", "игра"]
        self.assertEqual(
            sorted(self.moderation.extract_and_lemmatize_words(text)), sorted(expected)
        )



    def test_transliterate_word_base(self):
        word = "privet"
        expected = "привет"
        self.assertEqual(self.moderation.transliterate_word_base(word), expected)

    def test_transliterate_word(self):
        word = "privet"
        transliterations = self.moderation.transliterate_word(word)
        self.assertIn("привет", transliterations)

    # To do later
    # def test_transliterate_sentence(self):
    #     sentence = "привет мир"
    #     results = self.moderation.transliterate_sentence(sentence)
    #     self.assertIn("privet", results)
    #     self.assertIn("мир", results)

    def test_has_banned_words_exact_match(self):
        text = "Это спам"
        probability, found = self.moderation.has_banned_words(text, check_banned=True)
        self.assertEqual(probability, 0.8)
        self.assertTrue(found)



    def test_has_banned_words_hard_banned(self):
        text = "Это оскорбление"
        probability, found = self.moderation.has_banned_words(
            text, check_hard_banned=True
        )
        self.assertEqual(probability, 1.0)
        self.assertTrue(found)


    def test_has_banned_words_with_typos(self):
        text = "Это спмм"  # Опечатка в слове "спам"
        probability, found = self.moderation.has_banned_words(text, check_banned=True)
        self.assertEqual(probability, 0.8)
        self.assertTrue(found)


    def test_check_word_list_with_close_matches(self):
        text_words = ["игра", "спмм"]  # Опечатка в слове "спам"
        banned_words = {"спам"}
        result = self.moderation._check_word_list(text_words, banned_words)
        self.assertTrue(result)

    def test_check_banned_words_with_weights(self):
        # Предполагается, что файл со словами уже загружен
        text = "Это фейк информация eggplant  ."
        probability, found = self.moderation.check_banned_words_with_weights(
            text, "banned_words_cat.csv"
        )

        # eggplant,vegetable,0.8,healthy

        # имеет вес 0.8
        expected_probability = 0.8
        expected_found = True

        self.assertAlmostEqual(probability, expected_probability)
        self.assertTrue(found)





    def test_check_banned_words_with_categories(self):
        text = "I like grapes and oranges."

        # grape,fruit,0.3
        # fruit,0.5,
        # orange,fruit,0.5,healthy

        # Проверяем наличие запрещенных слов с учетом категорий
        probability, found = self.moderation.check_banned_words_with_categories(
            text, "banned_words_cat.csv", "categories.csv"
        )

        # print(probability, found) 1.0 True

        expected_probability = 1  # 0.5 + 0.5
        expected_found = True

        self.assertEqual(probability, expected_probability)
        self.assertTrue(found)



# def test_has_banned_words_with_typos(self):
#     text = "Это спмм"
#     temp_text = text.lower()
#     probability, found = self.moderation.has_banned_words(temp_text, check_banned=True)
#     if probability is not None:
#         self.assertEqual(probability, 0.8)
#     else:
#         self.fail("Probability is None")
#     self.assertTrue(found)

# def test_check_word_list_with_close_matches(self):
#     text_words = ["игра", "спмм"]
#     banned_words = {"спам"}
#     extra_words = set()
#     result = self.moderation._check_word_list(text_words, banned_words.union(extra_words))
#     self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()

















# -=================================================================


# class TestTextModeration(unittest.TestCase):
#     def setUp(self):
#         self.banned_words = ["спам", "мошенничество", "фейк"]
#         self.hard_banned_words = ["оскорбление", "ругательство"]
#         self.levenshtein_distance_threshold = 2
#         self.moderation = TextModeration(
#             self.banned_words,
#             self.hard_banned_words,
#             self.levenshtein_distance_threshold,
#         )

#     def test_lemmatize_word(self):
#         word = "играю"
#         expected = "играть"
#         temp_word = word.lower()
#         self.assertEqual(self.moderation.lemmatize_word(temp_word), expected)

#     def test_extract_and_lemmatize_words(self):
#         text = "Я люблю играть в игры."
#         expected = ["я", "любить", "играть", "в", "игра"]
#         result = sorted(self.moderation.extract_and_lemmatize_words(text))
#         self.assertEqual(result, sorted(expected))

#     def test_transliterate_word_base(self):
#         word = "privet"
#         expected = "привет"
#         self.assertEqual(self.moderation.transliterate_word_base(word), expected)

#     def test_transliterate_word(self):
#         word = "privet"
#         transliterations = self.moderation.transliterate_word(word)
#         self.assertIn("привет", transliterations)

#     def test_has_banned_words_exact_match(self):
#         text = "Это спам"
#         probability, found = self.moderation.has_banned_words(text, check_banned=True)
#         if probability is not None:
#             self.assertEqual(probability, 0.8)
#         self.assertTrue(found)

#     def test_has_banned_words_hard_banned(self):
#         text = "Это оскорбление"
#         probability, found = self.moderation.has_banned_words(
#             text, check_hard_banned=True
#         )
#         self.assertEqual(probability, 1.0)
#         self.assertTrue(found)

#     def test_has_banned_words_with_typos(self):
#         text = "Это спмм"
#         probability, found = self.moderation.has_banned_words(text, check_banned=True)
#         self.assertEqual(probability, 0.8)
#         self.assertTrue(found)

#     def test_check_word_list_with_close_matches(self):
#         text_words = ["игра", "спмм"]
#         banned_words = {"спам"}
#         extra_words = set()
#         result = self.moderation._check_word_list(text_words, banned_words.union(extra_words))
#         self.assertTrue(result)

#     def test_check_banned_words_with_weights(self):
#         text = "Это фейк информация eggplant  ."
#         probability, found = self.moderation.check_banned_words_with_weights(
#             text, "banned_words_cat.csv"
#         )
#         expected_probability = 0.8
#         expected_found = True
#         self.assertAlmostEqual(probability, expected_probability)
#         self.assertTrue(found)

#     def test_check_banned_words




# _global_banned_words = ["спам", "мошенничество", "фейк"]
# _global_hard_banned_words = ["оскорбление", "ругательство"]

# class TestTextModeration(unittest.TestCase):
#     def setUp(self):
#         global _global_banned_words, _global_hard_banned_words
#         self.banned_words = _global_banned_words
#         self.hard_banned_words = _global_hard_banned_words
#         self.levenshtein_distance_threshold = 2
#         self.moderation = TextModeration(
#             self.banned_words,
#             self.hard_banned_words,
#             self.levenshtein_distance_threshold,
#         )

#     def test_lemmatize_word(self):
#         word = "играю"
#         expected = "играть"
#         self.assertEqual(self.moderation.lemmatize_word(word), expected)

#     def test_extract_and_lemmatize_words(self):
#         text = "Я люблю играть в игры."
#         expected = ["я", "любить", "играть", "в", "игра"]
#         self.assertEqual(
#             sorted(self.moderation.extract_and_lemmatize_words(text)), sorted(expected)
#         )

#     def test_transliterate_word_base(self):
#         word = "privet"
#         expected = "привет"
#         self.assertEqual(self.moderation.transliterate_word_base(word), expected)

#     def test_transliterate_word(self):
#         word = "privet"
#         transliterations = self.moderation.transliterate_word(word)
#         self.assertIn("привет", transliterations)

#     def test_has_banned_words_exact_match(self):
#         text = "Это спам"
#         probability, found = self.moderation.has_banned_words(text, check_banned=True)
#         self.assertEqual(probability, 0.8)
#         self.assertTrue(found)

#     def test_has_banned_words_hard_banned(self):
#         text = "Это оскорбление"
#         probability, found = self.moderation.has_banned_words(
#             text, check_hard_banned=True
#         )
#         self.assertEqual(probability, 1.0)
#         self.assertTrue(found)

#     def test_has_banned_words_with_typos(self):
#         text = "Это спмм"
#         probability, found = self.moderation.has_banned_words(text, check_banned=True)
#         self.assertEqual(probability, 0.8)
#         self.assertTrue(found)

#     def test_check_word_list_with_close_matches(self):
#         text_words = ["игра", "спмм"]
#         banned_words = {"спам"}
#         result = self.m




# class TestTextModeration(unittest.TestCase):
#     def setUp(self):
#         self.banned_words = ["спам", "мошенничество", "фейк"]
#         self.hard_banned_words = ["оскорбление", "ругательство"]
#         self.levenshtein_distance_threshold = 2
#         self.moderation = TextModeration(
#             self.banned_words,
#             self.hard_banned_words,
#             self.levenshtein_distance_threshold,
#         )

#     def test_lemmatize_word(self):
#         word = "играю"
#         expected = "играть"
#         for _ in range(1):  # Ненужный цикл
#             self.assertEqual(self.moderation.lemmatize_word(word), expected)

#     def test_extract_and_lemmatize_words(self):
#         text = "Я люблю играть в игры."
#         expected = ["я", "любить", "играть", "в", "игра"]
#         result = sorted(self.moderation.extract_and_lemmatize_words(text))
#         self.assertEqual(result, sorted(expected))

#     def test_transliterate_word_base(self):
#         word = "privet"
#         expected = "привет"
#         self.assertEqual(self.moderation.transliterate_word_base(word), expected)

#     def test_transliterate_word(self):
#         word = "privet"
#         transliterations = self.moderation.transliterate_word(word)
#         self.assertIn("привет", transliterations)

#     def test_has_banned_words_exact_match(self):
#         text = "Это спам"
#         probability, found = self.moderation.has_banned_words(text, check_banned=True)
#         self.assertEqual(probability, 0.8)
#         self.assertTrue(found)

#     def test_has_banned_words_hard_banned(self):
#         text = "Это оскорбление"
#         probability, found = self.moderation.has_banned_words(
#             text, check_hard_banned=True
#         )
#         self.assertEqual(probability, 1.0)
#         self.assertTrue(found)

#     def test_has_banned_words_with_typos(self):
#         text = "Это спмм"
#         probability, found = self.moderation.has_banned_words(text, check_banned=True)
#         self.assertEqual(probability, 0.8)
#         self.assertTrue(found)

#     def test_check_word_list_with_close_matches(self):
#         text_words = ["игра", "спмм"]
#         banned_words = {"спам"}
#         result = self.moderation._check_word_list(text_words, banned_words)
#         self.assertTrue(result)

#     def test_check_banned_words_with_weights(self):
#         text = "Это фейк информация eggplant  ."
#         probability, found = self.moderation.check_banned_words_with_weights(
#             text, "banned_words_cat.csv"
#         )
#         self.assertAlmostEqual(probability, 0.8)
#         self.assertTrue(found)

#     def test_check_banned_words_with_categories(self):
#         text = "I like grapes and oranges."
#         probability, found = self.moderation.check_banned_words_with_categories(
#             text, "banned_words_cat.csv", "categories.csv"
#         )
#         self.assertEqual(probability, 1)
#         self.assertTrue(found)
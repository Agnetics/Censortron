from src.text_moderation import TextModeration

if __name__ == "__main__":
    blocked_csv_dir = (
        r"C:\Users\Tseh\Documents\Files\NeuroDeva\NetTyan\docker\filter\block_words"
    )
    banned_words_file = blocked_csv_dir + "/banned_words_cat_2_2.csv"

    categories_file = blocked_csv_dir + "/categories_2.csv"

    text_moderation = TextModeration(
        banned_words=[],
        hard_banned_words=[],
        levenshtein_distance_threshold=0.5,
    )

    test_cases = [
        ("I like jfdkhwemvsddsfd kfdjfkjdsfasssaqng.", 0.6, True),
        ("I like  президент  пробный текст эксперимент слово.", 0.35, True),
        ("gривет", 0.35, True),
        # ("I like grapes and oranges.", 0.3, True),  #
    ]

    for input_text, expected_probability, expected_found in test_cases:
        probability, has_banned = text_moderation.check_banned_words_with_categories(
            input_text, banned_words_file, categories_file
        )
        print(
            f"Input: {input_text}\nTotal Probability: {probability}, Expected: {expected_probability}, Found Banned Words: {has_banned}, Expected Found: {expected_found}\n"
        )





# _blocked_csv_dir = r"C:\Users\Tseh\Documents\Files\NeuroDeva\NetTyan\docker\filter\block_words"
# _banned_words_file = _blocked_csv_dir + "/banned_words_cat_2_2.csv"
# _categories_file = _blocked_csv_dir + "/categories_2.csv"

# if __name__ == "__main__":
#     global _text_moderation
#     _text_moderation = TextModeration(
#         banned_words=[],
#         hard_banned_words=[],
#         levenshtein_distance_threshold=0.5,
#     )

#     test_cases = [
#         ("I like jfdkhwemvsddsfd kfdjfkjdsfasssaqng.", 0.6, True),
#         ("I like президент пробный текст эксперимент слово.", 0.35, True),
#         ("gривет", 0.35, True),
#     ]

#     for input_text, expected_probability, expected_found in test_cases:
#         probability, has_banned = _text_moderation.check_banned_words_with_categories(
#             input_text, _banned_words_file, _categories_file
#         )
#         print(f"Input: {input_text}\nTotal Probability: {probability}, Expected: {expected_probability}, Found Banned Words: {has_banned}, Expected Found: {expected_found}\n")


# blocked_csv_dir = r"C:\Users\Tseh\Documents\Files\NeuroDeva\NetTyan\docker\filter\block_words"
#     banned_words_file = blocked_csv_dir + "/banned_words_cat_2_2.csv"
#     categories_file = blocked_csv_dir + "/categories_2.csv"

#     text_moderation = TextModeration(
#         banned_words=[],
#         hard_banned_words=[],
#         levenshtein_distance_threshold=0.5,
#     )

#     test_cases = [
#         ("I like jfdkhwemvsddsfd kfdjfkjdsfasssaqng.", 0.6, True),
#         ("I like президент пробный текст эксперимент слово.", 0.35, True),
#         ("gривет", 0.35, True),
#     ]

#     for input_text, expected_probability, expected_found in test_cases:
#         for _ in range(1):  # Н
# #             probability, has_banned = text_moderation.check_banned_words_with_categories(
# #                 input_text, banned_words_file, categories_file
# #             )
# #         print(f"Input: {input_text}\nTotal Probability: {probability}, Expected: {expected_probability}, Found Banned Words: {has_banned}, Expected Found: {expected_found}\n")


# from src.text_moderation import TextModeration

# def process_test_case(text_moderation, banned_words_file, categories_file, test_cases):
#     if not test_cases:
#         return
#     input_text, expected_probability, expected_found = test_cases[0]
#     probability, has_banned = text_moderation.check_banned_words_with_categories(
#         input_text, banned_words_file, categories_file
#     )
#     print(f"Input: {input_text}\nTotal Probability: {probability}, Expected: {expected_probability}, Found Banned Words: {has_banned}, Expected Found: {expected_found}\n")
#     process_test_case(text_moderation, banned_words_file, categories_file, test_cases[1:])

# if __name__ == "__main__":
#     blocked_csv_dir = r"C:\Users\Tseh\Documents\Files\NeuroDeva\NetTyan\docker\filter\block_words"
#     banned_words_file = blocked_csv_dir + "/banned_words_cat_2_2.csv"
#     categories_file = blocked_csv_dir + "/categories_2.csv"

#     text_moderation = TextModeration(
#         banned_words=[],
#         hard_banned_words=[],
#         levenshtein_distance_threshold=0.5,
#     )

#     test_cases = [
#         ("I like jfdkhwemvsddsfd kfdjfkjdsfasssaqng.", 0.6, True),
#         ("I like президент пробный текст эксперимент слово.", 0.35, True),
#         ("gривет", 0.35, True),
#     ]

#     process_test_case(text_moderation, banned_words_file, categories_file, test_cases)
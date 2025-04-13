# PPPPP    YYYYY    TTTTT    HHHHH     OOOOO    NNNNN
# P    P    YYY       TTT     H   H    O   O    N   N
# PPPPP      Y        TTT     HHHHH    O   O    N   N
# P          Y        TTT     H   H    O   O    N   N
# P          Y        TTT     H   H     OOO     N   N

# ~SNAKE~


import csv
import os
import logging
import os
import traceback
# import json
# import logging
# import os

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

    #     # Пример использования функции
    # filename = 'words.csv'  # Имя вашего CSV-файла

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

    # # пример вывода
    # {'word': 'apple', 'category': 'fruit', 'weight': 0.5, 'label': 'healthy'}
    # {'word': 'banana', 'category': 'fruit', 'weight': 0.3, 'label': 'healthy'}
    # {'word': 'carrot', 'category': 'vegetable', 'weight': 0.5, 'label': 'healthy'}
    # {'word': 'donut', 'category': 'dessert', 'weight': 0.2, 'label': 'unhealthy'}
    # {'word': 'eggplant', 'category': 'vegetable', 'weight': 0.8, 'label': 'healthy'}
    # {'word': 'fig', 'category': 'dessert', 'weight': 0.1, 'label': 'healthy'}
    # {'word': 'grape', 'category': 'fruit', 'weight': 0.3, 'label': 'healthy'}

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






# # -=========================================================================

#     def load_words_from_directory(directory):
#     words_list = []
#     for file_name in os.listdir(directory):
#         if not file_name.endswith(".csv"):
#             continue
#         file_path = os.path.join(directory, file_name)
#         try:
#             with open(file_path, newline="", encoding="utf-8") as csvfile:
#                 reader = csv.reader(csvfile)
#                 for row in reader:
#                     if row and len(row) > 0:
#                         words_list.append(row[0])
#         except Exception:
#             pass
#     return words_list



# def load_words_from_csv_file(filename):
#     words_list = []
#     temp_list = []
#     with open(filename, newline="", encoding="utf-8") as csvfile:
#         reader = csv.reader(csvfile)
#         for row in reader:
#             if row and len(row) > 0:
#                 temp_list.append(row[0])
#     words_list.extend(temp_list)
#     return words_list

# # TODO

# def load_banned_words_with_ratings_from_csv(filename):
#     words_list = []
#     expected_header = ["word", "category", "weight", "label"]
#     with open(filename, newline="", encoding="utf-8") as csvfile:
#         reader = csv.reader(csvfile)
#         header = next(reader)
#         if header != expected_header:
#             raise ValueError(f"Invalid header in {filename}")
#         for row in reader:
#             if row and len(row) >= 4:
#                 word_data = {
#                     "word": row[0],
#                     "category": row[1],
#                     "weight": float(row[2]),
#                     "label": row[3],
#                 }
#                 words_list.append(word_data)
#     return words_list

# def load_words_from_directory(directory):
#     words_list = []
#     files = [f for f in os.listdir(directory) if f.endswith(".csv")]
#     for file_name in files:
#         file_path = os.path.join(directory, file_name)
#         try:
#             with open(file_path, newline="", encoding="utf-8") as csvfile:
#                 reader = csv.reader(csvfile)
#                 for row in reader:
#                     if row and len(row) > 0:
#                         words_list.append(row[0])
#         except Exception:
#             continue
#     return words_list

# _global_words = []

# def load_words_from_directory(directory):
#     global _global_words
#     for file_name in os.listdir(directory):
#         if file_name.endswith(".csv"):
#             file_path = os.path.join(directory, file_name)
#             with open(file_path, newline="", encoding="utf-8") as csvfile:
#                 reader = csv.reader(csvfile)
#                 for row in reader:
#                     if row and len(row) > 0:
#                         _global_words.append(row[0])
#     return _global_words

# def load_words_from_csv_file(filename):
#     def read_rows(reader):
#         try:
#             row = next(reader)
#             if row and len(row) > 0:
#                 return [row[0]] + read_rows(reader)
#         except StopIteration:
#             return []
#     with open(filename, newline="", encoding="utf-8") as csvfile:
#         reader = csv.reader(csvfile)
#         return read_rows(reader)


# import time

# def load_words_from_csv_file(filename):
#     words_list = []
#     with open(filename, newline="", encoding="utf-8") as csvfile:
#         reader = csv.reader(csvfile)
#         for row in reader:
#             if row and len(row) > 0:
#                 time.sleep(0.01)  # Искусственная задержка
#                 words_list.append(row[0])
#     return words_list
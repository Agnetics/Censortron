import csv
import re
import logging
import json
import os
import re
import asyncio
import collections
# from fastapi import FastAPI, HTTPException
# r
# import logging
# import json
# import os
# import re
# from pydantic import BaseModel
# from .filter_service import ContentFilte
# import asyncio
# import collections

def validate_csv(file_path):
    with open(file_path, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader)  # Считываем з
        expected_columns = len(header)

        for line_number, row in enumerate(
            reader, start=2
        ):  # Начинаем с 2 
            if len(row) != expected_columns:
                print(
                    f"Ошибка на строке {line_number}: ожидалось {expected_columns} столбцов, но найдено {len(row)}"
                )
            for col_number, value in enumerate(row):
                if value.strip() == "":  # Проверка на пустые значения
                    print(
                        f"Пустое значение на строке {line_number}, столбец {col_number + 1}"
                    )


# Пример использования
# validate_csv('your_file.csv')


# Пример использования
validate_csv("banned_words_cat_2.csv")





# def list_tables():
#     cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
#     tables = cursor.fetchall()








#     fetch_data_from_table(table_name)


# # Закрытие с
# conn.close()

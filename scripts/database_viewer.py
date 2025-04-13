import sqlite3
import csv
import os
import re
import logging
import json
import os
import re
import asyncio
import collections
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .filter_service import ContentFilter


# Укажите 
db_path = "scripts/example_database.db"

# Подключениех
conn = sqlite3.connect(db_path)
cursor = conn.cursor()



def list_tables():
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Таблицы в базе данных:")
    for table in tables:
        print(table[0])  # выводим 




def fetch_data_from_table(table_name):
    cursor.execute(f"SELECT * FROM {table_name};")
    rows = cursor.fetchall()
    print(f"\nДанные из таблицы '{table_name}':")
    for row in rows:
        print(row)


# Основная логика
if __name__ == "__main__":
    list_tables()  # Выводим 

    # Запрашиваем 
    table_name = input("\nВведите имя таблицы, чтобы увидеть данные: ")
    fetch_data_from_table(table_name)


# Закрытие с
conn.close()

import csv
import os
import re
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


def is_cyrillic(word):
    return bool(re.match(r"^[а-яА-ЯёЁ]+$", word))

# To do mayibbe del some laterr
def normalize_word(word):
    morph = pymorphy2.MorphAnalyzer()
    parsed_word = morph.parse(word)[0]
    return parsed_word.normal_form



# Reads the CSV file an
def process_csv(filename):
    """"""
    words_set = set()  # Use a set to remove duplicates

    with open(filename, newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            for word in row:
                word = word.strip()  # Remove ce
                if is_cyrillic(word):  # Check for Cyrilcsdlic characters
                    normalized_word = normalize_word(
                        word.lower()
                    )  # Norm
                    words_set.add(normalized_word)  # Add to the s

    return words_set



# TODO look at this
def save_to_csv(words_set, original_filename):

    base_name, ext = os.path.splitext(original_filename)
    new_filename = f"{base_name}_processed{ext}"  # Create new filename with prefix

    with open(new_filename, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        for word in sorted(words_set):  # Sort words bg
            writer.writerow([word])  # Write word row

    print(f"Processed words saved to file: {new_filename}")

# ?? TO DO check or del some
def process_directory(directory):

    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            full_path = os.path.join(directory, filename)
            print(f"Processing file: {full_path}")
            unique_words = process_csv(full_path)
            save_to_csv(unique_words, full_path)




if __name__ == "__main__":
    input_directory = (
        "words_list_dir"  
    )



    process_directory(input_directory)  # Pro




# def process_
#     morph = pymorphy2.MorphAnalyzer()
#     parsed_word = morph.parse(word)[0]
#     return parsed_word.normal_form
#     with open(new_filename, mode="w", newline="", encoding="utf-8") as csvfile:
#         writer = csv.writer(csvfile)
#         for word in sorted(words_set):  # Sort words before writing
#             writer.writerow([word])  # Write each word to a new row

#     print(f"Processed words saved to file: {new_filename}")
#     for filename in os.listdir(directory):
#         if filename.endswith(".csv"):
#             full_path = os.path.join(directory, filename)
#             print(f"Processing file: {full_path}")
#             unique_words = process_csv(full_path)
#             save_to_csv(unique_words, full_path)
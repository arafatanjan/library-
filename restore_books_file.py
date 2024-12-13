import json
import os

def restore_all_books(all_books):
     file_name = "all_books.json"
     if not os.path.exists(file_name):
        print(f"{file_name} not found. Initializing with an empty list.")
        return []     
     with open(file_name, "r") as fp:
        all_books = json.load(fp)
     return all_books
import json
from datetime import datetime, timedelta
import os

def lend_book(all_books):
    
    borrowed_books_file = "borrowed_books.json"
    borrowed_books = []
    if os.path.exists(borrowed_books_file):
        with open(borrowed_books_file, "r") as fp:
            borrowed_books = json.load(fp)

    
    borrower_name = input("Enter borrower's name: ")
    borrower_phone = input("Enter borrower's phone number: ")
    book_title = input("Enter the book title to borrow: ")

    
    for book in all_books:
        if book["title"].lower() == book_title.lower():
            if book["quantity"] > 0:
                book["quantity"] -= 1

                
                due_date = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")

                
                borrowed_books.append({
                    "borrower_name": borrower_name,
                    "borrower_phone": borrower_phone,
                    "book_title": book_title,
                    "due_date": due_date
                })
                print(f"Book '{book_title}' has been lent to {borrower_name}. Due date: {due_date}.")

                # Save updates to files
                with open(borrowed_books_file, "w") as fp:
                    json.dump(borrowed_books, fp, indent=4)

                with open("all_books.json", "w") as fp:
                    json.dump(all_books, fp, indent=4)

                return
            else:
                print("There are not enough books available to lend.")
                return

    print(f"Book '{book_title}' not found in the library.")

import json
import os


def return_book(all_books):
    
    borrowed_books_file = "borrowed_books.json"
    borrowed_books = []

    # Restore borrowed books from file
    if os.path.exists(borrowed_books_file):
        with open(borrowed_books_file, "r") as fp:
            borrowed_books = json.load(fp)

    borrower_name = input("Enter your name: ")
    book_title = input("Enter the book title you are returning: ")

    for borrowed in borrowed_books:
        if borrowed["borrower_name"].lower() == borrower_name.lower() and borrowed["book_title"].lower() == book_title.lower():
            
            borrowed_books.remove(borrowed)

            # Increase the book quantity
            for book in all_books:
                if book["title"].lower() == book_title.lower():
                    book["quantity"] += 1
                    break

           
            with open(borrowed_books_file, "w") as fp:
                json.dump(borrowed_books, fp, indent=4)

            with open("all_books.json", "w") as fp:
                json.dump(all_books, fp, indent=4)

            print(f"Book '{book_title}' has been returned successfully.")
            return

    print("No matching record found for this return.")

from datetime import datetime

def add_book(library, book):
    book["date_added"] = datetime.now().strftime("%m-%d-%Y")
    library.append(book)

def load_library(library, loader):
    library.clear()
    library.extend(loader())
    print("\nLibrary Loaded")

def view_library(library):
    if not library:
        print("\nLibrary is empty.")
        return

    for number, book in enumerate(library, start=1):
        print(f"\n{number}. {book['title']}")

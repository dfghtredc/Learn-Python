import os

#Gets the folder where your current script lives
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#BuildS the path to the data folder 
FOLDER_FOR_DATA = os.path.join(BASE_DIR, "data")

os.makedirs(FOLDER_FOR_DATA, exist_ok=True)

# points to library.txt file
DATA_FILE = os.path.join(FOLDER_FOR_DATA, "library.txt")


def save_txt(library):
    
    with open(DATA_FILE, 'w') as file:

        for book in library:
            file.write(
                f"Book ID: {book['id']}\n"
                f"Title: {book['title']}\n"
                f"Author: {book['author']}\n"
                f"Genre: {book['genre']}\n"
                f"Year: {book['year']}\n"
                f"Status: {book['status']}\n"
                f"Date Added: {book['date_added']}\n\n"
            )

    print("\nLibrary Exported.")


def load_txt():

    books = []

    try:
        with open(DATA_FILE, 'r') as file:
            book = {}

            for line in file:
                
                if line.strip() == "":
                    if book:
                        books.append(book)
                        book = {}
                    
                    continue
                    
                parts = line.split(":", 1)

                if parts[0] == "Book ID":
                    book["id"] = parts[1].strip()

                elif parts[0] == "Title":
                    book["title"] = parts[1].strip()

                elif parts[0] == "Author":
                    book["author"] = parts[1].strip()

                elif parts[0] == "Genre":
                    book["genre"] = parts[1].strip()

                elif parts[0] == "Year":
                    book["year"] = parts[1].strip()

                elif parts[0] == "Status":
                    book["status"] = parts[1].strip()
                
                elif parts[0] == "Date Added":
                    book["date_added"] = parts[1].strip()

            if book:
                books.append(book)   
                
        return books
             
    except FileNotFoundError:
        if not books:
            print("No books found.")
        return books
    
    except IndexError:
        print("Invalid TXT Format.")
        return []
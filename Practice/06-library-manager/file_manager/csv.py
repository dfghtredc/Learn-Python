import os
import csv

#Gets the folder where your current script lives
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#BuildS the path to the data folder 
FOLDER_FOR_DATA = os.path.join(BASE_DIR, "data")

os.makedirs(FOLDER_FOR_DATA, exist_ok=True)

# points to library.txt file
DATA_FILE = os.path.join(FOLDER_FOR_DATA, "library.csv")

def save_csv(library):

    with open(DATA_FILE, 'w', encoding="utf-8", newline="") as file:
        fieldnames = [
            "id",
            "title",
            "author",
            "genre",
            "year",
            "status",
            "date_added"
            ]
        
        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )
        writer.writeheader()

        for book in library:
            writer.writerow(book)
    print("\nLibrary Exported.")        

def load_csv():
    books = []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                books.append(row)

        print(f"\nLibrary Loaded.")
        return books

    except FileNotFoundError:
        print(f"File not found") 
        return[]

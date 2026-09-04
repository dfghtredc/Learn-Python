from library import add_book
from ui import title, get_input

def add_book_menu(library):

    fields = [
        "id",
        "title",
        "author",
        "genre",
        "year",
        "status",
    ]

    book = {}

    title("Add Book Menu")
    print(f"If unknown leave it Blank")

    index = 0

    while index < len(fields):

        field = fields[index]

        value = get_input(f"{field}: ")

        if value is None:
            print("Book Creation Cancelled. ")
            return

        if value.lower() == "prev":
            if index > 0:
                index -=1
            else:
                print("You are at the first field.")
            continue
        
        book[field] = value

        index += 1

    add_book(library, book)
    print(f"\nAdded: {book['title']}")
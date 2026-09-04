EDITABLE_FIELDS = [
    "title",
    "author",
    "genre",
    "year",
    "status"
]

def edit_book(library):

    if not library:
        print("Library is empty")
        return

    for number, book in enumerate(library, start=1):
        print(f"{number}. {book['title']} by {book['author']}")

    
    choice = input("\nEnter Book Number (or back): ")

    if choice.lower() == "back":
        return  
    
    try:
        selected_book = int(choice)

    except ValueError:
        print("Please enter a valid number.")
        return 

    if selected_book < 1 or selected_book > len(library):
        print("Invalid Book Number")
        return
    
    book = library[selected_book - 1]

    
    print("\nEditable Fields: ")

    for field in EDITABLE_FIELDS:
        print(field.capitalize())

    field = input("\nField to edit: ").lower()

    if field not in EDITABLE_FIELDS:
        print("Invalid Field")
        return

    new_value = input("New Entry: ")

    if not new_value:
        print("Value cannot be empty.")
        return

    book[field] = new_value
    
    print(f"'{book['title']}' updated successfully.")
   

          
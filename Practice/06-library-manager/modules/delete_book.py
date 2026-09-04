def delete_book(library):

    if not library:
        print("Library is empty.")
        return

    for number, book in enumerate(library, start=1):
        print(f"{number}. {book['title']} by {book['author']}")

    delete_choice = input("\nEnter Book Number (or back): ")

    if delete_choice.lower() == "back":
        return  
    
    try:
        deleted_book = int(delete_choice)

    except ValueError:
        print("Please enter a valid number.")
        return 

    if deleted_book < 1 or deleted_book > len(library):
        print("Invalid Book Number")
        return
    
    else:
        deleted = library.pop(deleted_book - 1)
        print(f"\nBook {deleted['title']} has been deleted.")
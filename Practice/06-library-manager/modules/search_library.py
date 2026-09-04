from ui import title, search_menu, get_input

def search_library(library):
    while True:
        title("Search Library")

        search_menu()

        menu_touch = get_input("Enter Here: ")

        if menu_touch == "BACK":
                return

        if menu_touch == "PREV":
                continue

        if menu_touch == "1":
            field = "title"

        elif menu_touch == "2":
            field = "author"
        
        elif menu_touch == "3":
            field = "year"
        
        elif menu_touch == "4":
            return

        else: 
            print("Invalid Choice")
            continue

        search_text = get_input ("Search: ").lower() 

        if search_text == "BACK":
            return

        if search_text == "PREV":
            continue 
        
        results = []

        for book in library:
            if search_text in book[field].lower():
                results.append(book)

        if not results:
            print("No Books Found.")
            continue

        for number, book in enumerate(results, start=1):
            print(
                f"{number}. {book['title']} by {book['author']}"
            )


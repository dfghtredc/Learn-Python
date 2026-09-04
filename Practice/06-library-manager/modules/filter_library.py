from ui import title, get_input, filter_library_menu


def filter_library(library):

    while True:
        title("Filter Library")

        if not library:
            print("Library is empty.")
            return

        filter_library_menu()

        menu_touch = get_input("Enter Here: ")

        if menu_touch == "BACK":
                return

        if menu_touch == "PREV":
                continue

        if menu_touch == "1":
            field = "id"

        elif menu_touch == "2":
            field = "title"
        
        elif menu_touch == "3":
            field = "author"
        
        elif menu_touch == "4":
            field = "genre"

        elif menu_touch == "5":
            field = "year"

        elif menu_touch == "6":
            field = "status"
        
        elif menu_touch == "7":
            return

        else: 
            print("Invalid Choice")
            continue

        values = set()

        for book in library:
            values.add(book[field])

        values = list(values)

        for number, value in enumerate(values, start=1):
            print(f"{number}. {value}")

        selected_value = get_input("\nEnter Here: ")

        if selected_value == "BACK":
            return

        if selected_value == "PREV":
            continue

        try:
            choice = int(selected_value)
            selected_value = values[choice - 1]

        except (ValueError, IndexError):
            print("Invalid Choice.")
            continue


        results = []

        for book in library:
            if book[field] == selected_value:
                results.append(book)


        if not results:
            print("No books found.")
            continue


        print("\nBooks Found:")

        for number, book in enumerate(results, start=1):
            print(f"{number}. {book['title']} by {book['author']}")
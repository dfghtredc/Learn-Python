def title(text):
    print("\n" + "=" * 30)
    print(text)
    print("="*30)

def pause():
    input("\nPress Enter to continue....")

def show_main_menu():
    print("""
    [1] Add Book
    [2] Edit Book
    [3] Delete Book
    [4] View Library
    [5] Search Library
    [6] Filter Library
    [7] Export TXT
    [8] Export CSV
    [9] Export JSON
    [10] Export Database
    [11] Load TXT
    [12] Load CSV
    [13] Load JSON
    [14] Load Database
    [15] Exit
    """)

def get_choice(prompt="\nEnter Here: ", minimum=1, maximum=15):
    
    while True:
        try:
            choice = int(input(prompt))

            if choice < minimum or choice > maximum:
                print(f"Choose Between {minimum}-{maximum}")
                continue
        
            return choice

        except ValueError:
            print("Please enter a number.")

def get_input(prompt):
    while True:
        value = input(prompt)

        if value.lower() == "back":
            return "BACK"

        if value.lower() == "prev":
            return "PREV"
        
        return value


def search_menu():
    print("""
    Search By:
    [1] Title
    [2] Author
    [3] Publication Year
    [4] Back 
    """)

def filter_library_menu():
    print("""
    Filter By:
    [1] ID
    [2] Title
    [3] Author
    [4] Genre
    [5] Year
    [6] Status
    [7] Back
    """)
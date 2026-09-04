import file_manager
import modules
from library import load_library, view_library
from library_data import library
from ui import get_choice, pause, show_main_menu, title


def main_menu():
    while True:
        title("Main Menu")

        show_main_menu()

        menu_pick = get_choice()

        if menu_pick == 1:
            modules.add_book_menu(library)
            pause()

        elif menu_pick == 2:
            modules.edit_book(library)
            pause()

        elif menu_pick == 3:
            modules.delete_book(library)
            pause()

        elif menu_pick == 4:
            view_library(library)
            pause()

        elif menu_pick == 5:
            modules.search_library(library)
            pause()

        elif menu_pick == 6:
            modules.filter_library(library)
            pause()

        elif menu_pick == 7:
            file_manager.save_txt(library)
            pause()

        elif menu_pick == 8:
            file_manager.save_csv(library)
            pause()

        elif menu_pick == 9:
            file_manager.save_json(library)
            pause()

        elif menu_pick == 10:
            file_manager.save_database(library)
            pause()

        elif menu_pick == 11:
            load_library(library, file_manager.load_txt)
            pause()

        elif menu_pick == 12:
            load_library(library, file_manager.load_csv)
            pause()

        elif menu_pick == 13:
            load_library(library, file_manager.load_json)
            pause()

        elif menu_pick == 14:
            load_library(library, file_manager.load_database)
            pause()

        elif menu_pick == 15:
            print("\nBye Bye")
            break

from display import main_menu
from file_manager.database import initialize_database


def main():
    initialize_database()
    main_menu()




if __name__ == "__main__":
    main()

"""
Possible Future Update:
    - Display only unread books.
    - Automatically save changes.
    - Export reports.
    - Save book ratings (1–5 stars).
    - Create backup files.
"""
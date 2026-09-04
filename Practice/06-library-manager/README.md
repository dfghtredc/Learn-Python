# Library Manager

A command-line Library Manager built with Python. The project allows users to create, view, edit, delete, search, and filter books while supporting multiple methods of storing and loading the library.

The project was created as a Python learning project to practice functions, modules, file I/O, data structures, error handling, and SQLite databases.

## Features

### Book Management

* Add books
* View the library
* Edit existing books
* Delete books
* Search books
* Filter books by different fields
* Return to previous menus with `BACK`/`PREV` commands
* Cancel operations when appropriate
* Track when books were added

### Data Storage

The library supports multiple storage formats:

* TXT
* CSV
* JSON
* SQLite

This allows the same library collection to be exported to different formats and loaded back into the application.

### SQLite Database

The SQLite database provides persistent database storage with:

* A `books` table
* Unique book IDs
* Book information stored in columns
* Book creation/addition dates
* SQL queries for retrieving books
* Database loading and saving
* Automatic database/table initialization

### User Interface

The application uses a separate UI module to handle presentation-related functionality, including:

* Menu titles
* Main menu
* Search menu
* Filter menu
* Input handling
* Pause functionality
* Consistent menu formatting

## How It Works

The application uses a modular structure where different parts of the program have different responsibilities.

The general flow is:

```text
main.py
   ↓
display.py
   ↓
modules / file_manager
   ↓
library data
```

For example, when adding a book:

```text
User
 ↓
Add Book Menu
 ↓
Collect book information
 ↓
add_book()
 ↓
library list
```

When saving to SQLite:

```text
library
 ↓
save_database()
 ↓
SQLite
 ↓
library.db
```

When loading from SQLite:

```text
library.db
 ↓
load_database()
 ↓
Python dictionaries
 ↓
library list
```

## Book Data Structure

Books are represented as Python dictionaries.

Example:

```python
{
    "id": "B001",
    "title": "The Hobbit",
    "author": "J.R.R. Tolkien",
    "genre": "Fantasy",
    "year": "1937",
    "status": "Read",
    "date_added": "08-07-2026"
}
```

The `library` itself is a list containing these dictionaries:

```python
library = [
    {
        "id": "B001",
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "genre": "Fantasy",
        "year": "1937",
        "status": "Read",
        "date_added": "08-07-2026"
    }
]
```

Keeping all storage methods based around the same book structure allows TXT, CSV, JSON, and SQLite to work with the same library data.

## File Organization

```text
06-library-manager/
│
├── main.py
├── display.py
├── ui.py
│
├── library.py
│
├── modules/
│   ├── __init__.py
│   ├── add_book.py
│   ├── edit_book.py
│   ├── delete_book.py
│   ├── search.py
│   └── filter.py
│
├── file_manager/
│   ├── __init__.py
│   ├── txt.py
│   ├── csv.py
│   ├── json.py
│   └── database.py
│
└── data/
    ├── library.txt
    ├── library.csv
    ├── library.json
    └── library.db
```

## File Responsibilities

### `main.py`

The entry point of the application.

It starts the program and calls the main menu.

```python
if __name__ == "__main__":
    main()
```

### `display.py`

Handles the main application flow.

It connects the menus and library functions together.

Responsibilities include:

* Main menu
* Add Book menu
* Loading libraries
* Calling save/load functions
* Connecting user choices to application functions

### `ui.py`

Contains reusable user-interface functions.

Examples:

* `title()`
* `pause()`
* `get_input()`
* `get_choice()`
* Menu display functions

Keeping UI code separate prevents `display.py` and the modules from becoming filled with repeated formatting code.

### `library.py`

Contains the core library data and library-related operations.

The main library is represented by:

```python
library = []
```

Functions in this area work with the collection of books.

### `modules/`

Contains individual book-management features.

Examples:

```text
add_book.py
edit_book.py
delete_book.py
search.py
filter.py
```

Each module focuses on a specific task instead of putting all functionality into one large file.

### `file_manager/`

Contains the different storage systems.

```text
txt.py
csv.py
json.py
database.py
```

Each module provides functions for saving and/or loading the library.

For example:

```python
save_txt()
load_txt()

save_csv()
load_csv()

save_json()
load_json()

save_database()
load_database()
```

### `data/`

Contains the actual saved library data.

```text
library.txt
library.csv
library.json
library.db
```

These files are generated/used by the file-management modules.

## Main Menu

The application currently provides options similar to:

```text
==============================
Main Menu
==============================

    [1] Add Book
    [2] Edit Book
    [3] Delete Book
    [4] View Library
    [5] Search Library
    [6] Filter Library
    [7] Export TXT
    [8] Export CSV
    [9] Export JSON
    [10] Save SQLite
    [11] Load TXT
    [12] Load CSV
    [13] Load JSON
    [14] Load SQLite
    [15] Exit
```

The exact menu numbers may change as the project develops.

## Adding a Book

Selecting `Add Book` prompts the user for information such as:

```text
id:
title:
author:
genre:
year:
status:
```

The application supports navigation commands such as:

```text
back
prev
```

`back` can cancel the current operation, while `prev` can return to a previous field where supported.

## Editing a Book

The Edit Book feature first displays the books:

```text
1. The Hobbit by J.R.R. Tolkien
2. Dune by Frank Herbert
3. Atomic Habits by James Clear
```

The user selects a book and then chooses which field to modify.

Editable fields include:

```text
Title
Author
Genre
Year
Status
```

The book dictionary is then updated directly.

## Deleting a Book

The Delete Book feature displays the library and allows the user to select a book by number.

The selected dictionary is removed from the `library` list.

## Searching

The Search feature allows the user to search the library using book information.

For example:

```text
Search By:
[1] Title
[2] Author
[3] Back
```

The search compares the user's input against the selected field and returns matching books.

## Filtering

The Filter feature allows the user to choose a field first:

```text
Filter By:
[1] ID
[2] Title
[3] Author
[4] Genre
[5] Year
[6] Status
[7] Back
```

The application then determines the unique values for that field.

For example, filtering by genre might produce:

```text
1. Fantasy
2. Science Fiction
3. Biography
4. History
```

Selecting a value displays all books matching that value.

This approach makes the filter system reusable instead of having a separate function for every possible field.

## Data Formats

### TXT

The TXT format stores books in a human-readable format.

Example:

```text
Book ID: B001
Title: The Hobbit
Author: J.R.R. Tolkien
Genre: Fantasy
Year: 1937
Status: Read
```

### CSV

CSV stores the library in rows and columns.

```text
id,title,author,genre,year,status
B001,The Hobbit,J.R.R. Tolkien,Fantasy,1937,Read
```

This format is useful for spreadsheet programs and tabular data.

### JSON

JSON represents the library using structured data.

Example:

```json
[
    {
        "id": "B001",
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "genre": "Fantasy",
        "year": "1937",
        "status": "Read"
    }
]
```

### SQLite

SQLite stores the library in a relational database.

The main table is:

```text
books
```

with columns such as:

```text
id
title
author
genre
year
status
date_added
```

The `id` column is the primary key, meaning every book must have a unique ID.

## SQLite Architecture

The database module separates database operations into individual functions.

```text
initialize_database()
        ↓
Creates books table if necessary

save_database(library)
        ↓
Stores books in SQLite

load_database()
        ↓
Retrieves books from SQLite
```

SQLite rows are converted back into Python dictionaries so that the rest of the application can continue using the same `library` structure.

## Running the Application

From the project directory, run:

```bash
python main.py
```

or:

```bash
python3 main.py
```

The application will start at the main menu.

## Requirements

The project currently uses Python's standard library.

Important modules include:

```python
os
json
csv
sqlite3
datetime
```

No external Python packages are required for the core application.

## Data Safety

The TXT, CSV, JSON, and SQLite files are separate storage systems.

Exporting to one format does not automatically update the others.

For example:

```text
library
   ├── export → TXT
   ├── export → CSV
   ├── export → JSON
   └── save → SQLite
```

The application must explicitly save/export the current library when changes need to be persisted.

## Project Goals

This project is primarily a Python learning project.

It is designed to practice:

* Variables
* Lists
* Dictionaries
* Loops
* Conditional statements
* Functions
* Function parameters
* Return values
* Exception handling
* File I/O
* TXT files
* CSV files
* JSON
* SQLite
* SQL queries
* Modules
* Packages
* Imports
* Code organization
* Refactoring
* Reusable functions
* Data conversion
* Basic application architecture

## Future Improvements

Possible future features include:

* Duplicate-book detection
* Better input validation
* Database updates instead of only inserts
* Database deletion
* Database searching with SQL
* Database filtering with SQL
* Sorting books
* Multiple library collections
* Book ratings
* Reading progress
* Pagination for large libraries
* Improved terminal UI
* Configuration files
* Automated tests
* Logging
* Backup and restore functionality
* Importing data between TXT, CSV, JSON, and SQLite
* Better database error handling

## Current Architecture

The project is gradually moving toward a separation of responsibilities:

```text
                    main.py
                       │
                       ▼
                  display.py
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
         ui.py      modules/    file_manager/
                       │            │
                       │       ┌────┼────┬────┐
                       │       ▼    ▼    ▼    ▼
                       │      TXT  CSV JSON SQLite
                       │
                       ▼
                  library data
```

The goal is to keep each part of the application responsible for one type of work rather than putting the entire program into one file.

## Roadmap

### Core Library Management

* [x] Add books
* [x] View library
* [x] Edit books
* [x] Delete books
* [x] Track date added
* [x] Cancel book creation
* [x] Navigate between fields with `PREV`
* [x] Return to previous menus with `BACK`

### Search & Filtering

* [x] Search by title
* [x] Search by author
* [x] Filter library
* [x] Filter by ID
* [x] Filter by title
* [x] Filter by author
* [x] Filter by genre
* [x] Filter by year
* [x] Filter by status

### File Storage

* [x] TXT export
* [x] TXT loading
* [x] CSV export
* [x] CSV loading
* [x] JSON export
* [x] JSON loading
* [x] Organized `data/` directory
* [x] Separate file-manager modules

### SQLite Database

* [x] Create SQLite database
* [x] Create `books` table
* [x] Save library to SQLite
* [x] Load library from SQLite
* [x] Use SQLite primary keys
* [x] Store `date_added`
* [ ] Update existing database records
* [ ] Delete database records
* [ ] Prevent duplicate records when saving
* [ ] Search directly with SQL
* [ ] Filter directly with SQL

### Code Organization

* [x] Separate UI functions
* [x] Separate book-management modules
* [x] Separate file-management modules
* [x] Use `__init__.py` for packages
* [x] Reduce duplicated code
* [x] Create reusable input functions
* [ ] Further refactor `display.py`
* [ ] Improve separation between application logic and UI
* [ ] Create shared database utilities

### Validation & Error Handling

* [x] Handle invalid menu input
* [x] Handle invalid book numbers
* [x] Handle invalid fields
* [x] Handle missing files
* [x] Handle invalid JSON
* [x] Handle permission errors
* [x] Handle empty libraries
* [ ] Validate book IDs
* [ ] Prevent duplicate book IDs before saving
* [ ] Validate publication years
* [ ] Validate reading status
* [ ] Improve database error handling

### Testing

* [ ] Create unit tests
* [ ] Test book creation
* [ ] Test editing
* [ ] Test deletion
* [ ] Test searching
* [ ] Test filtering
* [ ] Test TXT storage
* [ ] Test CSV storage
* [ ] Test JSON storage
* [ ] Test SQLite storage
* [ ] Test invalid input
* [ ] Add automated testing with `pytest`

### User Interface

* [x] Create reusable menu formatting
* [x] Create reusable titles
* [x] Create reusable input functions
* [x] Add pause functionality
* [ ] Improve terminal layout
* [ ] Add better status messages
* [ ] Add confirmation prompts for destructive actions
* [ ] Improve error messages
* [ ] Add sorting options
* [ ] Add pagination for large libraries

### Future Features

* [ ] Book ratings
* [ ] Reading progress
* [ ] Favorites
* [ ] Multiple library collections
* [ ] Import between TXT, CSV, JSON, and SQLite
* [ ] Database backup and restore
* [ ] Automatic backups
* [ ] Configuration file
* [ ] Logging
* [ ] Statistics and library summaries
* [ ] Advanced search
* [ ] Advanced filtering
* [ ] Export reports

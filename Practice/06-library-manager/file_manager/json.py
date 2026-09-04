import os
import json

#Gets the folder where your current script lives
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#BuildS the path to the data folder 
FOLDER_FOR_DATA = os.path.join(BASE_DIR, "data")

os.makedirs(FOLDER_FOR_DATA, exist_ok=True)

# points to library.txt file
DATA_FILE = os.path.join(FOLDER_FOR_DATA, "library.json")

def save_json(library):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(library,
        file, 
        indent=4,
        ensure_ascii=False
        )
    
    print("\nLibrary Exported.")

def load_json():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

            if not isinstance(data, list):
                print("Invalid Library Format.")
                return []
            
            return data
    
    except FileNotFoundError:
        print(f"File Not Found")
        return[]
    
    except json.JSONDecodeError:
        print(f"Invalid JSON Format.")
        return[]
    
    except PermissionError:
        print(f"Permission Denied.")
        return[]
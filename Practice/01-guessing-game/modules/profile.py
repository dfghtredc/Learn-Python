def profile():
    name = input("What is your name? \nEnter: ")
    age = int(input("\nHow old are you? \nEnter: "))
    height = input("\nHow tall are you? \nEnter: ")
    weight = float(input("\nHow much do you weigh? \nEnter: "))
    hair = input("\nWhat color is your hair? \nEnter: ")
    eye = input("\nWhat color are your eyes? \nEnter: ")

    profile = {
        "name": name,
        "age": age,
        "height": height,
        "weight": weight,
        "hair": hair,
        "eye": eye,
    }

    return profile

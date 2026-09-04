import modules
import ui

user_profile = modules.profile()

print(f"\nWelcome to my game, {user_profile['name']}.")
print("You only get 10 tries.")

ui.main_menu_display()

play_again = True

while play_again:
    choice = input("\nEnter your choice: ")

    if choice == "1":
        modules.start_game()

        answer = input("\nWould you like to play again? ").lower()

        if answer == "no":
            play_again = False

    elif choice == "2":
        print("Change difficulty")

    elif choice == "3":
        print(user_profile)

    elif choice == "4":
        print("Stats")

    elif choice == "5":
        print(f"Bye Bye {user_profile['name']}!")
        play_again = False

    else:
        print("Invalid choice. Please select 1-5.")

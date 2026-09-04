import random


def start_game():
    print("\nGame starting.........\n")

    secret = random.randint(1,100)

    won = False
    max_attempts = 10
    attempts = 0

    while attempts < max_attempts: 
        guess = float(input("Enter a Number: "))
        attempts +=1
        
        if guess < secret:
            print("Too Low. Guess Again.")
            
        elif guess > secret:
            print("Too High. Guess Again.")
        
        else:
            won = True
            print("OMG YOU DID WOWWWW, YOU BEAT ME")
            print(f"It took you {attempts} guesses.")
            break
    if not won:
        print(f"You ran out of attempts. The secret number was {secret}")
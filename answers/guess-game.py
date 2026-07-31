# NUMBER GUESSING GAME
# I made this after learning loops and conditionals
# It took me like 2 hours to get right lol

import random

# Welcome message
print("=" * 40)
print("   WELCOME TO THE NUMBER GUESSING GAME!")
print("=" * 40)
print("\nI'm thinking of a number between 1 and 100...")
print("You have 7 guesses. Good luck!\n")

# Generate random number
secret_number = random.randint(1, 100)
guesses_left = 7
guesses_taken = 0

# I used a while loop here because I don't know how many tries it'll take
while guesses_left > 0:
    print(f"Guesses remaining: {guesses_left}")
    
    # Get user input - had to add try/except because user kept crashing it with letters
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("⚠️  Please enter a valid number! Try again.\n")
        continue
    
    guesses_taken += 1
    guesses_left -= 1
    
    # Check the guess
    if guess < secret_number:
        print("📈 Too low! Go higher.")
    elif guess > secret_number:
        print("📉 Too high! Go lower.")
    else:
        # They got it right!
        print("\n🎉🎉🎉 CORRECT! 🎉🎉🎉")
        print(f"You got it in {guesses_taken} tries!")
        break
    
    # Give a hint if they're running out of guesses - I added this later
    if guesses_left == 2:
        if secret_number % 2 == 0:
            print("💡 HINT: The number is even")
        else:
            print("💡 HINT: The number is odd")
    
    print()  # empty line for spacing

# If they run out of guesses
if guesses_left == 0 and guess != secret_number:
    print("\n😢 Oh no! You ran out of guesses.")
    print(f"The number was {secret_number}. Better luck next time!")

print("\nThanks for playing! 🎮")
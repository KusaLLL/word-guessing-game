import random

name = input("What's your name? ")
print("Good luck, ", name)

words = ['python', 'c++', 'java', 'kotlin', 'c', 'sql', 'javascript', 'r', 'ruby']
answer = random.choice(words)

if answer == words[0]:
    print("HINT: Most popular computer language")
elif answer == words[1]:
    print("HINT: PLUS PLUS!!")
elif answer == words[2]:
    print("HINT: Widely used for enterprise applications")
elif answer == words[3]:
    print("HINT: Best way to learn OOP")
elif answer == words[4]:
    print("HINT: Single-letter language")
elif answer == words[5]:
    print("HINT: The God of databases")
elif answer == words[6]:
    print("HINT: Widely used in web development")
elif answer == words[7]:
    print("HINT: A popular language for data science")
elif answer == words[8]:
    print("HINT: Starts with 'R' and great for stats")

print("\nGuess the characters:")

user_inputs = ''
turns = 12

while turns > 0:
    failed = 0

    # Print the current state of the guessed word
    for char in answer:
        if char in user_inputs:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1

    print()

    # Check if the user has won
    if failed == 0:
        print("You won! Congratulations!")
        print(f"The word is: {answer}")
        break

    # Input the next character
    guess = input("Enter a character: ")
    user_inputs += guess

    # Check if the guess is in the answer
    if guess not in answer:
        turns -= 1
        print("Wrong guess!")
        print(f"You have {turns} more guesses.")

    if turns == 0:
        print("You lost! The word was:", answer)

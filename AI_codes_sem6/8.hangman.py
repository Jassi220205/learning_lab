import random

# Word list
words = ["python", "machine", "learning", "artificial", "intelligence", "algorithm"]

word = random.choice(words)
guessed_letters = []
attempts = 6

display_word = ["_"] * len(word)

print("Welcome to Hangman")

while attempts > 0 and "_" in display_word:

    print("\nWord:", " ".join(display_word))
    print("Attempts left:", attempts)

    guess = input("Enter a letter: ").lower()

    # Validation
    if len(guess) != 1 or not guess.isalpha():
        print("Enter a single alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
    else:
        print("Wrong guess.")
        attempts -= 1


# Game result
if "_" not in display_word:
    print("\nYou won!")
    print("The word was:", word)
else:
    print("\nYou lost!")
    print("The word was:", word)
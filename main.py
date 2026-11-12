import random

word = random.choice(["python", "hangman", "puzzle"])
guessed = []
misses = 0

while misses < 6:
    print(" ".join(c if c in guessed else "_" for c in word))
    guess = input("Guess a letter: ")

    guessed.append(guess)

    if guess not in word:
        misses += 1

    # TODO: check if the player won
    # TODO: check for bad input
    # TODO: show a lose message

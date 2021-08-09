import random
import os
from images import images, hangman_title


easy_words = ["able", "acid", "aged", "also", "area", "army"]
medium_words = ["breath", "bridge", "bright", "broken", "budget", "burden"]
hard_words = ["enormous", "entirely", "entrance", "envelope", "equality",
              "equation"]
lives = 7
guessed = []
missed = []
game_complete = False
word = ""


def get_word():
    """
    Gets a random word based on the difficulty chosen
    """
    global word
    difficulty = input("Pick game difficulty (easy, medium, hard):\n").lower()
    if difficulty == "easy":
        word = random.choice(easy_words)
    elif difficulty == "medium":
        word = random.choice(medium_words)
    elif difficulty == "hard":
        word = random.choice(hard_words)
    else:
        print("Input not valid, please select a valid option")
        get_word()
    return word


def show_status(word, hidden):
    """
    Shows the hidden word and hangman image based on lives remaning
    """
    os.system("clear")
    print(hangman_title)
    print(images[7-lives])
    print()
    print(hidden)
    print()


def play(word, hidden):
    """
    Plays the game until word is guessed or no more lives remain
    """
    global guessed, missed, lives, game_complete
    while game_complete is False and lives > 0:
        guess = input("Guess a letter or the entire word: \n").lower()
        # Guess is a letter not already guessed
        if (len(guess) == 1 and guess.isalpha() and guess not in hidden
                and guess not in missed):
            if guess in word and not len(guessed) == len(word) - 1:
                occurences = find_occurrences(word, guess)
                for index in occurences:
                    hidden = hidden[:index] + guess + hidden[index + 1:]
                show_status(word, hidden)
                print(f"Well done, '{guess}' is part of the word!")
                for occurence in occurences:
                    for x in str(occurence):
                        guessed.append(x)
                print()
                print(f"Missed letters: {missed}")
                print(f"Lives remaining: {lives}")
                print()
            elif guess in word and len(guessed) == len(word) - 1:
                occurences = find_occurrences(word, guess)
                for index in occurences:
                    hidden = hidden[:index] + guess + hidden[index + 1:]
                show_status(word, hidden)
                print(f"Congratulations, the correct word was '{word}'!")
                print()
                print(f"Missed letters: {missed}")
                print(f"Lives remaining: {lives}")
                print()
                game_complete = True
            elif guess not in word and lives != 1:
                lives -= 1
                show_status(word, hidden)
                print(f"Sorry, '{guess}' is not part of the word. Try again.")
                missed.append(guess)
                print()
                print(f"Missed letters: {missed}")
                print(f"Lives remaining: {lives}")
                print()
            elif guess in guessed or guess in missed:
                print(f"You already guessed letter '{guess}'', try again.")
            else:
                lives -= 1
                show_status(word, hidden)
                print(f"Sorry, the correct word was '{word}'...")
                print()
                print(f"Missed letters: {missed}")
                print(f"Lives remaining: {lives}")
                print()
        # Guess is a letter that was already guessed
        elif guess.isalpha() and guess in hidden or guess in missed:
            show_status(word, hidden)
            print(f"Letter '{guess}' was already guessed, try again.")
            print()
            print(f"Missed letters: {missed}")
            print(f"Lives remaining: {lives}")
            print()
        # Guess is an entire word and is correct
        elif guess == word and guess.isalpha():
            if guess == word:
                hidden = word
                show_status(word, hidden)
                print(f"Congratulations, the correct word was '{word}'!")
                print()
                print(f"Missed letters: {missed}")
                print(f"Lives remaining: {lives}")
                print()
                game_complete = True
        # Guess is an entire word but is incorrect
        elif guess != word and guess.isalpha():
            if lives != 1:
                lives -= 1
                show_status(word, hidden)
                print(f"Sorry, '{guess}' is not the correct word...")
                print()
                print(f"Missed letters: {missed}")
                print(f"Lives remaining: {lives}")
                print()
            else:
                lives -= 1
                show_status(word, hidden)
                print(f"Sorry, the correct word was '{word}'...")
                print()
                print(f"Missed letters: {missed}")
                print(f"Lives remaining: {lives}")
                print()
        # Handles incorrect value input
        else:
            show_status(word, hidden)
            print("Invalid input, only letters are accepted...")
            print()
            print(f"Missed letters: {missed}")
            print(f"Lives remaining: {lives}")
            print()


def find_occurrences(s, ch):
    """
    Finds occurrencies of the letter that was guessed in the word
    """
    return [i for i, letter in enumerate(s) if letter == ch]


def new_game():
    """
    Starts a new game or exit the program based on user choice
    """
    global lives, guessed, missed, game_complete
    print()
    play_again = input("Would you like to play again? (yes/no)\n").lower()
    if play_again == "yes":
        lives = 7
        guessed = []
        missed = []
        game_complete = False
        word = get_word()
        hidden = (len(word) * "-")
        show_status(word, hidden)
        play(word, hidden)
        new_game()
    if play_again == "no":
        print("Thanks for playing!!")
        raise SystemExit
    else:
        print("Input invalid. Please enter a valid option...")
        new_game()


def main():
    """
    Run program functions
    """
    print(hangman_title)
    print("Welcome to Hangman! Guess all the letters and reveal the word!\n")
    word = get_word()
    hidden = (len(word) * "-")
    show_status(word, hidden)
    play(word, hidden)
    new_game()


main()

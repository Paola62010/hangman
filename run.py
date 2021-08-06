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
hidden = (len(word) * "_")


def get_word():
    global word
    difficulty = input("Select game difficulty: easy, medium, hard:\n")
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


def show_status(word):
    os.system("clear")
    print(hangman_title)
    print(images[7-lives])
    print()
    print(hidden)
    print()
    print(word)


def play():
    global guessed, missed, lives, game_complete, hidden
    while game_complete is False and lives > 0:
        guess = input("Guess a letter or the entire word: \n").lower()
        if (len(guess) == 1 and guess.isalpha() and guess not in hidden
                and guess not in missed):
            if guess in word and not len(guessed) == len(word) - 1:
                occurences = find_occurrences(word, guess)
                for index in occurences:
                    hidden = hidden[:index] + guess + hidden[index + 1:]
                show_status(word)
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
                show_status(word)
                print(f"Congratulations, the correct word was '{word}'!")
                game_complete = True
            elif guess not in word and lives != 1:
                lives -= 1
                show_status(word)
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
                show_status(word)
                print(f"Sorry, the correct word was '{word}'...")
        elif guess in hidden or guess in missed:
            print(f"Letter '{guess}' was already guessed, try again.")
        elif guess == word and guess.isalpha():
            if guess == word:
                show_status(word)
                print(f"Congratulations, the correct word was '{word}'!")
                game_complete = True
        elif guess != word and guess.isalpha():
            if lives != 1:
                lives -= 1
                show_status(word)
                print(f"Sorry, '{guess}' is not the correct word")
                print()
                print(f"Missed letters: {missed}")
                print(f"Lives remaining: {lives}")
                print()
            else:
                lives -= 1
                show_status(word)
                print(f"Sorry, the correct word was '{word}'...")

        else:
            show_status(word)
            print("Invalid input, only letters are accepted")


def find_occurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]


def new_game():
    global lives, guessed, missed, game_complete, hidden, word
    print()
    play_again = input("Would you like to play again? (yes/no)\n").lower()
    if play_again == "yes":
        lives = 7
        guessed = []
        missed = []
        game_complete = False
        word = get_word()
        hidden = (len(word) * "_")
        play()
    if play_again == "no":
        print("Thanks for playing!!")
        pass
    else:
        print("Input invalid. Please enter a valid option.")
        new_game()


def main():
    print(hangman_title)
    print("Welcome to Hangman! Guess all the letters and reveal the word!\n")
    word = get_word()
    show_status(word)
    play()
    #new_game()


main()

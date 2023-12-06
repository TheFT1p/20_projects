# Write your code here
import random

hangman0 = r"""
    _____
    |   |
    |  
    |   
    |  
________________
"""
hangman1 = r"""
    _____
    |   |
    |  \
    |   
    |   
________________
"""
hangman2 = r"""
    _____
    |   |
    |  \ /
    |   
    |  
________________
"""
hangman3 = r"""
    _____
    |   |
    |  \o/
    |   
    |  
________________
"""
hangman4 = r"""
    _____
    |   |
    |  \o/
    |   |
    |  
________________
"""
hangman5 = r"""
    _____
    |   |
    |  \o/
    |   |
    |  / 
________________
"""

hangman6 = r"""
    _____
    |   |
    |  \o/
    |   |
    |  / \
________________
"""

list_hangman = [hangman0, hangman1, hangman2, hangman3, hangman4, hangman5, hangman6]
word_list = ['TopKek', 'Cartman', 'AyyLMAO', 'Dnevnik', 'Praksa']  # ADD POSSIBILITY TO INPUT A SENTENCE


def display_hangman(error_count):
    print(list_hangman[error_count])


def get_valid_guess(guessed_letters):
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha() and guess not in guessed_letters:
            return guess
        else:
            print("Please enter a valid, single letter that you have'nt already guessed so far.")


if __name__ == '__main__':
    error_count = 0
    word = random.choice(word_list)
    duzina = len(word)
    print(word)
    guessed_letters = set()
    so_far = "_" * duzina
    so_far_list = list(so_far)
    while "_" in so_far_list and error_count < 6:
        guess = get_valid_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess.lower() in word.lower():
            for i in range(len(word)):
                if guess.lower() == word[i].lower():
                    so_far_list[i] = guess
            print(f"Correct! Guess another character!\n{''.join(so_far_list)}")
        else:
            error_count += 1
            display_hangman(error_count)
    if '_' not in so_far_list:
        print(f"You won! The word is {''.join(so_far_list)}! You saved the hangee!")
    else:
        print(f"you fucked up. Word WAS {word}")

# if __name__ == '__main__':
#     error_count = 0
#     word = random.choice(word_list)
#     duzina = len(word)
#     print(word)
#     guessed_letters = set()
#     so_far = "_" * duzina
#     so_far_list = list(so_far)
#     while "_" in so_far_list and error_count < 6:
#         slovo = input("Guess the character: ").lower()
#         if slovo.lower() in word.lower():
#             for i in range(len(word)):
#                 if slovo == word[i].lower():
#                     so_far_list[i] = slovo.lower()
#             print(f"Correct! Guess another character!\n{''.join(so_far_list)}")
#         else:
#             error_count += 1
#             print(list_hangman[error_count])
#     else:
#         if "_" not in so_far_list:
#             print(f"You won! The word is {''.join(so_far_list)}! You've saved our hangee")
#         else:
#             print(f"Too bad! The guy is hanged! .. Also, the word WAS {word}")


"""SO FAR SO GOOD.
Improvement requirements:
    -Add Functions for checking and repetitive tasks    DONE
    -Handle input validation through function           DONE
    -Improve user interface                             DONE
    -Allow Phrases
    -Also, try INDEX(), REPLACE() and str.maketrans(char_to_replace, replacement_char)
    -dne____. Make it look like Dne____, while user can STILL input 'd'


    example:
            original_string = "Daewoo"
            char_to_replace = "o"
            replacement_char = "_"

            translation_table = str.maketrans(char_to_replace, replacement_char)
            updated_string = original_string.translate(translation_table)

            print(f"The updated string is: {updated_string}")

"""

import random

hangman_figures = [
    r"""
        _____
        |   |
        |  
        |   
        |  
    ____________________
    """,
    # Add other hangman figures...
]


def display_hangman(error_count):
    print(hangman_figures[error_count])


def get_valid_guess(guessed_letters):
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha() and guess not in guessed_letters:
            return guess
        else:
            print("Please enter a valid, single letter that you haven't guessed before.")


if __name__ == '__main__':
    error_count = 0
    word = random.choice(word_list).lower()
    duzina = len(word)
    print(word)
    guessed_letters = set()
    so_far = "_" * duzina

    while "_" in so_far and error_count < 6:
        guess = get_valid_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in word:
            for i in range(len(word)):
                if guess == word[i]:
                    so_far_list[i] = guess
            print(f"Correct! Guess another character!\n{''.join(so_far_list)}")
        else:
            error_count += 1
            display_hangman(error_count)

    if "_" not in so_far_list:
        print(f"You won! The word is {''.join(so_far_list)}! You've saved our hangee")
    else:
        print(f"Too bad! The guy is hanged! .. Also, the word WAS {word}")

#

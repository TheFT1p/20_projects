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
word_list = ['TopKek', 'Cartman', 'AyyLMAO', 'Dnevnik', 'Praksa'] #ADD POSSIBILITY TO INPUT A SENTENCE



if __name__ == '__main__':
    error_count = 0
    word = random.choice(word_list)
    duzina = len(word)
    print(word)
    so_far = "_" * duzina
    so_far_list = list(so_far)
    while "_" in so_far_list and error_count < 6:
        slovo = input("Guess the character: ").lower()
        if slovo.lower() in word.lower():
            for i in range(len(word)):
                if slovo == word[i].lower():
                    so_far_list[i] = slovo.lower()
            print(f"Correct! Guess another character!\n{''.join(so_far_list)}")
        else:
            error_count += 1
            print(list_hangman[error_count])
    else:
        if "_" not in so_far_list:
            print(f"You won! The word is {''.join(so_far_list)}! You've saved our hangee")
        else:
            print(f"Too bad! The guy is hanged! .. Also, the word WAS {word}")

















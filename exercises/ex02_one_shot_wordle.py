"""One shot wordle!"""

__author__: (730656282)

white: str = "\U00002B1C"
yellow: str = "\U0001F7E8"
green: str = "\U0001F7E9"


# allowing guess and setting variables
secret_word: str = "python"
word_length: int = len(secret_word)
guess: str = input(f"What is your {word_length} -letter guess? ")
while len(guess) != word_length:
    guess = input(f"Oops! That's not {word_length} letters! Try Again: ")
# while loop, checking index of guessed word, printing box based on if in word
i: int = 0
box_string: str = " "
while i <= word_length - 1:
    if guess[i] == secret_word [i]:
        box_string = box_string + green
    else:
        guessed_letter_exists: bool = False
        alternate_indicies: int = 0
        while guessed_letter_exists is not True and alternate_indicies <= word_length - 1:
            if secret_word[alternate_indicies] == guess[i]:
                guessed_letter_exists = True
            else:
                alternate_indicies = alternate_indicies + 1
        if guessed_letter_exists is True:
            box_string = box_string + yellow
        else:
            box_string = box_string + white
    i = i + 1
# printing box result and guess result
print(box_string)
if guess != secret_word:
    print("Not quite. Play again soon! ")
else: 
    print("Woo! You got it!")
        

    

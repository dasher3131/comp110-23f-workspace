"""EX03 - Wordle!"""
__author__ = "730656282"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


# making function to test if guess has a correct character
def contains_char(user_guess: str, searched_character: str) -> bool:
    """Search through word to see if character is in guess."""
    assert len(searched_character) == 1
    i: int = 0
    # if searched letter is in word it will return true if not false
    while i <= len(user_guess) - 1:
        if user_guess[i] == searched_character:
            return True
        i += 1
    return False


# function that prints correct emoji boxes depending on characters in word.
def emojified(guess_word: str, secret_word: str) -> str:
    """Function to create emojis in right order."""
    assert len(guess_word) == len(secret_word)
    i: int = 0
    box_string: str = ""
    while i <= len(guess_word) - 1:
        if guess_word[i] == secret_word[i]:
            box_string += GREEN_BOX
        # calling function to see if letter is in word
        else:
            if contains_char(secret_word, guess_word[i]) is True:
                box_string += YELLOW_BOX
            else:
                box_string += WHITE_BOX
        i += 1
    return box_string


# Function to get length of word.
def input_guess(guess_length: int) -> str:
    """Make sure user guesses a word of correct length."""
    user_guess: str = input(f"Please enter a {guess_length} character word. ")
    while len(user_guess) != guess_length:
        user_guess = input(f"That wasn't {guess_length} chars! Try again: ")
    return user_guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    # Your code will go here
    turn_count: int = 1
    game_status: bool = False
    secret_word: str = "codes"
    user_input: str = ""
    box_string: str = ""
    # while loop to make sure turns is below 6 and game is not over
    while turn_count <= 6 and game_status is False:
        print(f"=== Turn {turn_count}/6 ===")
        user_input = input_guess(len(secret_word))
        box_string = emojified(user_input, secret_word)
        print(box_string)
        if user_input == secret_word:
            game_status = True
            print(f"You won in {turn_count} turns! ")
        else:
            if turn_count == 6:
                print("X/6 - Sorry, try again tomorrow!")
                game_status = True
            else:
                turn_count += 1


# added to make it able to run as module
if __name__ == "__main__":
    main()
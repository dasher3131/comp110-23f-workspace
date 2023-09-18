"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730656282"

wordle_word: str = input("Please enter a 5 character word. ")
if len(wordle_word) !=5: 
    print("Error: Word must contain 5 characters. ")
    exit()
letter_guess: str = input("Enter a single character. ")
if len(letter_guess) !=1:
    print("Error: Character must be a single character. ")
    exit()
else:
    print("Searching for " + letter_guess + " in " + wordle_word)\

instance_count: int = 0
if letter_guess == wordle_word[0] :
    print(letter_guess + " Found at index 0")
    instance_count = instance_count + 1
if letter_guess == wordle_word[1] :
    print(letter_guess + " Found at index 1")
    instance_count = instance_count + 1   
if letter_guess == wordle_word[2] :
    print(letter_guess + " Found at index 2")
    instance_count = instance_count + 1
if letter_guess == wordle_word[3] :
    print(letter_guess + " Found at index 3")
    instance_count = instance_count + 1
if letter_guess == wordle_word[4] :
    print(letter_guess + " Found at index 4")
    instance_count = instance_count + 1
if instance_count == 0:
    print("No instances of " + letter_guess + " found in " + wordle_word)
else:
    if instance_count == 1:
        print("1 instance of " + letter_guess + " found in " + wordle_word)
    else:
        if instance_count == 2:
            print("2 instances of " + letter_guess + " found in " + wordle_word)
        else:
            if instance_count == 3:
                print("3 instances of " + letter_guess + " found in " + wordle_word)
            else:
                if instance_count == 4:
                    print("4 instances of " + letter_guess + " found in " + wordle_word)
                else:
                    if instance_count == 5:
                        print("5 instances of " + letter_guess + " found in " + wordle_word)              

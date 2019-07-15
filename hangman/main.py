import random


print("Welcome to the hangman game!")
restart_game = True
while restart_game:
    word_bank = ["apple", "laptop", "python", "object", "spam", "nabbil"]
    word = random.choice(word_bank).lower()
    input_guess = None
    used_letters = []
    empty_word = []
    for i in word:
        empty_word.append("*")
    trys = 5

    while trys > 0:

        try:
            input_guess = str(input("Choose a letter but beware!".lower()))
        except:
            print("Nice try buddy but that is not a correct option")
            continue

        if (trys != 0 and "*" in empty_word):
            print("You have {} attempts remaining".format(trys))

        elif len(input_guess) > 1:
            print("What part of hangman do you not understand? GIVE ME ONLY ONE LETTER ")
            continue

        elif input_guess in used_letters:
            print("Wait a sec, you already tried that letter!")
            continue

        else:
            pass

        used_letters.append(input_guess)

        if input_guess not in word:
            trys -= 1
            print("Be careful! you're going to kill him!!!")
        else:
            print("".join(word))

    if trys == 0:
        print("GAME OVER loser! the word was ", word)
        print("Wana play again?")
        if response not in ("yes", "y"):
            restart_game = False
            print("Thanks for Playing you weirdo")
        break

    if "*" not in word:
        print("Congrats you have won the game!!")
        print("Would you like to test your luck again??")
        if response not in ("yes", "y"):
            restart_game = False
            print("Thanks for Playing you weirdo")
        breaka
        

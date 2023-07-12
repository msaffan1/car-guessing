# Matt Saffan
# This program asks the user to guess an exotic car manufacturer from a pre-determined word bank.

# import random to use random functions later
import random
# word bank of words that the user must guess
words = ["ferrari","mclaren","maserati","porsche","bugatti","pagani","bentley"]
# user can enter their username
# introduction prompt to explain what the user should do
name = input("Hey! I'm Percy the parrot but you can just call me Perry! Enter your name to begin! ")
print("Perry: Hi",name,"! Time to begin!")
def main():
    print("\n\t\t - Exotic Car Guessing Game - ")
    print("\nPerry: You have 10 attempts to guess the exotic vehicle manufacturer correctly.")
    #list to store wrong guessed letters
    incorrectList = []
    # pick random word from word bank
    originalWord = random.choice(words)
    print("The word has",len(originalWord), "letters.")
    # create an empty list to give hints to the user by replacing each letter of random word with _
    guessedWord = []
    for i in range(len(originalWord)):
        guessedWord.append("_")
    print(*([i for i in guessedWord]))
    # t is used as the amount of guesses available
    t = 15
    while (t):
        t = t-1
        # allow the user to guess a letter
        guessedLetter = input("Guess a letter: ")
        # check if guessedLetter is an alphabet, if not give error
        if not guessedLetter.isalpha():
            print("ERROR - That's not a letter!")
        # check if guessed letter length is singular, if not give error
        elif (len(guessedLetter)>1):
            print('ERROR - One letter at a time!')
        # check that letter chosen by user is already guessed or not
        elif (guessedLetter in incorrectList):
            print('ERROR - You already guessed this letter!')
        # check if guessed letter matches with the original word
        if guessedLetter in originalWord:
            for i in range(len(originalWord)):
                if originalWord[i] == guessedLetter:
                    guessedWord[i] = originalWord[i]
        else:
            # if guessed letter is not in the original word
            # tell the user the letter is incorrect
            print("You guessed an incorrect letter")
            incorrectList.append(guessedLetter)
        guessWord = [i for i in guessedWord]
        guessWord = "".join(guessedWord)

        # If the word is correctly guessed
        if originalWord == guessWord:
            print("Perry: That's correct! Congratulations!")
            print('These were the incorrect letters you guessed', incorrectList)
        # Asking the user if they want to play again
            replay = input('Did you want to play again? Press (y) or (n)')
            if replay == 'n':
                exit()
            if replay == 'y':
                main()
            else:
                exit()
        # print the guessed word
        print(*([i for i in guessWord]))
        # prompt user showing number of attempts left to win
        print("You have",t,"attempts left")
        # if the user runs out of guesses:
        if t == 0:
            if originalWord != guessedWord:
                print("Perry: SQUAWK!!! You lost the game ,the vehicle manufacturer was ",originalWord)
                print('These were the incorrect letters you guessed', incorrectList)

                # Asking the user if they want to play again
                replay = input('Did you want to play again? Press (y) or (n) ')
                if replay == 'n':
                    exit()
                if replay == 'y':
                    main()
                else:
                    exit()

main()
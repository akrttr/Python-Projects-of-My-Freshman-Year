import time
import sys


def readFileFunction():
    fileLetterValues = open(sys.argv[2], "r", encoding="utf-8-sig")  # Reading letter value file
    letterValues = fileLetterValues.readlines()
    pointOfLettersDict = {}
    for line in letterValues:  # Loop for letter value to create dictionary
        line = line.strip()
        line = line.replace("İ", "i").replace("I", "ı").lower()
        line = line.split(":")
        pointOfLettersDict[line[0]] = int(line[1])
    fileLetterValues.close()
    fileCorrectWords = open(sys.argv[1], "r", encoding="utf-8-sig")  # Reading correct_words file
    correctWords = fileCorrectWords.readlines()
    correctWordsDict = {}
    for line in correctWords:  # Loop for correct words to create dictionary
        line = line.strip()
        line = line.replace("İ", "i").replace("I", "ı").lower()
        items = line.split(":")
        correctWordsDict[items[0]] = items[1].split(",")
    fileCorrectWords.close()
    return correctWordsDict, pointOfLettersDict


def main():
    if len(sys.argv) != 3:  # Close the progran if there are not adequate command line arguments
        print("You must write two arguments for this program")
        return
    correctWordsDict, pointOfLettersDict = readFileFunction()
    for i in range(len(correctWordsDict.keys())):
        print("Shuffled letters are:\t{0}\tPlease guess words for these letters with minimum three letters".format(list(correctWordsDict.keys())[i]))
        control = []  # List for storing guessed words
        ctr = 0
        endTime = int(time.time()) + 30
        while ctr < len(list(correctWordsDict.values())[i]) and int(time.time()) < endTime:
            guessInput = input("Guessed Word: ").replace("İ", "i").replace("I", "ı").lower()  # Asking for a guess from user
            if guessInput in control:  # Checking input whether it is guessed before or not
                print("This word is guessed before")
            elif guessInput in list(correctWordsDict.values())[i]:  # Checking input whether it is valid or not
                control.append(guessInput)  # Appending control list wit correct words
                ctr += 1
            else:
                print("your guessed word is not a valid word") 
            print("You have {0} time".format(endTime - int(time.time())))
        score = 0  # Defining a variable to store user's score
        for word in control:  # Loop for calculating score letter by letter
            for letter in word:
                score += pointOfLettersDict[letter] * len(word)
        print("Score for {0} is {1} and guessed words are: {2}".format(list(correctWordsDict.keys())[i], score, str(control).strip("[]").replace("'", "").replace(", ", "-")))


main()

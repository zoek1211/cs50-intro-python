## Short dictionary methods

# replicate spelling bee game

WORDS = {"PAIR": 4, "HAIR": 3, "CHAIR": 5, "GRAPHIC": 7}

def main():
    print("Welcome to the Spelling Bee Game!")
    print("Your letters are: I I P C R H G")

    while len(WORDS) > 0:
        print(f"{len(WORDS)} words left!")
        guess = input("Guess a word: ")

        # check if guess is in dictionary
        # use guess as a key to access the value 
        if guess == "GRAPHIC":
            WORDS.clear() # remove all items from the dictionary
            print("You guessed the super word! You win!")

        if guess in WORDS.keys():
            points = WORDS.pop(guess) # return value associated with key and remove the key from the dictionary
            print(f"Good Job! You scored {points} points!")

    print("That's the game!")


def main():
    print("Welcome to the Spelling Bee Game!")
    WORDS.items() # return key value pairs as tuples
    for word, points in WORDS.items(): # key, value
        print(f"{word} is worth {points} points")


main()
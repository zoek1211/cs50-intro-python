import random

cards = ["jack", "queen", "king"]

def main():
    # choose one random card
    print(random.choice(cards))

    # print k number of cards 
    print(random.choices(cards, k=2))

    # shuffle the cards. two distinct cards
    print(random.sample(cards, k=2))

    # weight: always choose jack 
    print(random.choices(cards, weights=[100, 0, 0], k=2))

    random.seed(1) # Set seed for reproducibility stay consistent help debugging


main()


## list and dictionary comprehensions

def main():
    counts = {}
    words = get_words("address.txt")
    # convert all words to lowercase if length is greater than 4
    lowercase_words = [word.lower() for word in words if len(word) > 4] 

    # create a dictionary with words as keys and their counts as values
    # counts = {word: words.count(word) for word in lowercase_words}
    # for every word in lowercase, give me a key called word, and set the value to the count 
    counts = {word: words.count(word) for word in lowercase_words}

    for word in words:
        if word in counts:
            counts[word] +=1
        else:
            counts[word] = 1
    
    # save_counts(counts)



def get_words():
    ...
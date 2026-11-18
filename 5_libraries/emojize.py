# Because emoji aren’t quite as easy to type as text, at least on laptops and desktops, some programs support “codes,” whereby you can type, 
# for instance, :thumbs_up:, which will be automatically converted to 👍. 
# Some programs additionally support aliases, whereby you can more succinctly type, 
# for instance, :thumbsup:, which will also be automatically converted to 👍.

import emoji

def main():
    user_input = input("Input: ")
    emojized = emoji.emojize(user_input, language = "alias") # convert to emoji, allows for aliases
    print(emojized)

main()
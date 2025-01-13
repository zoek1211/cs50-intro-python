# side effects

emoticon = "v.v"

def main():
    global emoticon
    say("Is anyone there?")
    emoticon = ":D"
    say("Oh, hi!")

def say(phrase):
    print(phrase + " " + emoticon)


main()

# phrase local variable
# emoticon global variable
# make global variable modifiable by including global emotiocon in a function
# make sure it is good design
# hard to debug if variable gets modified across all functions
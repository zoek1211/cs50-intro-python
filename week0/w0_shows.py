# string methods

SHOWS = [
    " Avatar: the last airbender",
    "Ben 10",
    "Arthur",
    " Spongebog Squarepants",
    "Phineas and ferb",
    "Kim possible",
    "Jimmy Neutron",
    "the Proud family"
]

def main():
    cleaned_shows = []
    for show in SHOWS:
        cleaned_shows.append(show.strip().title())
    
   
    print(', '.join(cleaned_shows))

main()

# capitalize() only uppercases the first character
# title() capitalizes every word as title
# strip() removes spaces 
# when printing list, it shows quotes 
# ' '.join use string you want to use, joins together by that

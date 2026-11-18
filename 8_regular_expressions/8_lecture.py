# regular expressions regex

# regexes

email = input("What's your email? ").strip()

if "@" in email and "." in email : 
    print("valid")
else:
    print("invalid")


# alternative 
# return two parts: username, domain 
username, domain = email.split("@")

# if username has at least one character and domain has at least one character and a dot
if username and "." in domain: # two separate conditions. if username is not empty and domain contains a dot
    print("valid")
else:
    print("invalid")

# more specific
# username has at least one character and domain has at least one character and ends with .edu
if username and domain.endswith(".edu"): 
    print("valid")
else:
    print("invalid")


# re library for regular expression

# re.search(pattern, string, flags=0) 
# pattern is the regex pattern to search for
# string is the string to search within
# flags are optional and modify the search behavior

# pattern symbos
# . any character except a newline
# * 0 or more repetitions
# + 1 or more repetitions
# ? 0 or 1 repetition
# {m} exactly m repetitions
# {m,n} between m and n repetitions
# ^ start of string
# $ end of string
# [] set of characters
# [^] complementing the set of characters
# \d digit
# \D non-digit
# \s whitespace
# \S non-whitespace
# \w word character (alphanumeric + underscore)
# \W non-word character
# A|B either A or B
# ( ) grouping
# (?: ) non-capturing group



import re

# 0 or more character .+ or ..* 
# .*@.* means 0 or more characters before and after the @ symbol

# r before the string means raw string, so that backslashes are treated literally
# [^@] means any character except @
# + means one or more of the preceding element
# \. means a literal dot (since . is a special character in regex, we escape it with a backslash)
# $ means end of string
# if re.search(r"^[^@]+@[^@]+\.edu$", email): 
# [a-z A-Z 0-9] _ means alphanumeric characters and underscore
# or \w means word characters (alphanumeric and underscore)

# re.IGNORECASE or re.I makes the search case-insensitive
# re.MULTILINE or re.M allows ^ and $ to match the start and end of each line, not just the start and end of the string
# re.DOTALL or re.S makes the . special character match any character including a newline

# (\w+\.)? means an optional group of one or more word characters followed by a dot
if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE): 

    print("valid")
else: 
    print("invalid")

# re.match(pattern, string, flags=0)
# matches the pattern only at the beginning of the string

name = input("What's your name? ").strip()
if "," in name:
    last, first = name.split(", ")
    name = f"{first} {last}"
print(f"hello, {name}")

# use re
name = input("What's your name? ").strip()
# re.search(r"^(.+), *(.+)$", name)
if matches:= re.search(r"^(.+), *(.+)$", name):
    # last, first = matches.groups()
    # last = matches.group(1)
    # first = matches.group(2)
    name = matches.group(2) + " " + matches.group(1)
    name = f"{first} {last}"
print(f"hello, {name}")


url = input("URL: ").strip()

# username = url.replace("https://twitter.com/", "")
# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/(.+)$", "", url)

if matches := re.search(r"^https?://?(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print(f"username:", matches.group(1))






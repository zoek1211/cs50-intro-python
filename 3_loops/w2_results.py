## Short lists

results = ["Mario", "Luigi"]

# append method
results.append("Peach")  # add Peach to the end of the list
results.append("Yoshi")
results.append("Koopa Troopa")

results.append(["Bowser", "Donkey Kong"]) # this has brackets inside a list 
results.remove(["Bowser", "Donkey Kong"])
results.extend(["Bowser", "Donkey Kong"])  # add to the end of the list

results.remove("Koopa Troopa")  # remove Koopa Troopa from the list
results.insert(0, "Toad")  # insert Toad at the beginning of the list
results.reverse()  # reverse the order of the list
results.sort()  # sort the list in alphabetical order

print(results)
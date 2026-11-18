# Short Dictionaries

distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 54,
    "Parker Solar Probe": 0.01,
}

def main():
    for name in distances.keys(): # return all keys in the dictionary
        print(f"{name} is {distances[name]} AU from Earth") # acess value by key


def main():
    for distance in distances.values(): # return all values in the dictionary
        print(f"{distance} AU is {convert(distance)} m")


def convert(au):
    return au * 1495978070700


main()
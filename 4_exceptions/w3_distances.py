# handling exceptions

distances = {
    "voyager 1": "163",
    "voyager 2": "136",
    "Pioneer 10": "80 AU",
    "New Horizons": "58",
    "Pioneer 11": "44 AU"
}

def main():
    spacecraft = input("Enter a spacecraft: ")
    try:
        au = float(distances[spacecraft])
    except KeyError:
        print(f"'{spacecraft}' not found in dictionary")
        return
    except ValueError:
        print(f"Can't convert '{distances[spacecraft]}' to a float")
        return
    
    m = convert(au)
    print(f"{m} m away")

def convert(au):
    return au * 149597870700

main()

# anticipate exceptions and write code to handle them
# KeyError if spacecraft not found in dictionary
# ValueError if value can't be converted to float
# use try and except to handle exceptions
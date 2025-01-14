# suppose that you are in a country where it's customary to 
# eat breakfast between 7:00 and 8:00,
# lunch between 12:00 and 13:00
# dinner between 18:00 and 19:00
# prompt the user for a time and output whether it's breakfast time, lunch time, or dinner time
# if it's not time for meal, don't output anything at all
# assume the user input will be formatted in 24-hour time
# as #:## or ##:##
# assume that each meal's time range is inclusive
# for instance, whether it's 7:00, 7:01, 7:59, or 8:00, it's time for breakfast

def main():
    time = input("What time is it? ")

    convert(time)

def convert(time):
    hours, minutes = map(int, time.split(":"))

    time = hours + minutes / 60

    if 7 <= time <= 8:
            print("Breakfast time")
    elif 12 <= time <= 13:
            print("Lunch time")
    elif 18 <= time  <= 19:
            print("Dinner time")
    else:
          return None

if __name__ == "__main__":
    main()
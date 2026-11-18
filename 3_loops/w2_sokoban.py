## list methods

def main():
    history = []
    
    while True:
        action = input("Action: ")

        if action == "Undo":
            undone = history.pop() # remove last item from history
            print(f"Undone: {undone}")
        elif action == "Restart":
            history.clear() # remove all items from history
        else:
            history.append(action)

        print(history)


main()    
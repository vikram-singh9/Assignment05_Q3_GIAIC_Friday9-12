def main():
    affirmation =  "I am capable of doing anything I put my mind to."
    user = input(f"Enter the affirmation: {affirmation} ")
    while True:
        if user == affirmation:
            print("That's right!")
            break
        else:
            print("That's not right!")
            user = input(f"Enter the affirmation: {affirmation} ")

if __name__ == '__main__':
    main()
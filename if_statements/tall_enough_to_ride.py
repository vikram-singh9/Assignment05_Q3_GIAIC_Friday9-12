mini_height = 50

def main():
    user_height = float(input("Enter your height: ") )

    if user_height >= mini_height:
        print(f"You are tall enough to ride the roller coaster")
    else:
        print(f"You are not tall enough to ride the roller coaster")

if __name__ == '__main__':
    main()  
def main():
    while True:
        number1 = int(input("Enter the first number: "))
        number2 = int(input("Enter the second number: "))
        result = number1 / number2
        remainder = number1 % number2
        print(f"The result of this division is {result} and remainder is {remainder}")

if __name__ == "__main__":
    main()

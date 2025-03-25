def main():
    numbers: list[int] = [1, 2, 3, 4]  # Creates a list of numbers

    for i in range(len(numbers)):  # Iterates through the list
        elem = numbers[i]
        numbers[i] = elem * 2
        print(numbers)
        

    

if __name__ == '__main__':
    main()
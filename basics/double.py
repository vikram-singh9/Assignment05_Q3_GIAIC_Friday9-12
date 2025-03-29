def double_until_100():
    curr_value = int(input("Enter a number: "))
    while curr_value < 100:
        curr_value *= 2
        print(curr_value, end=" ")
    print()

double_until_100()

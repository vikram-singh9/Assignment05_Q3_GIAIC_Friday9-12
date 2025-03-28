def collect_values():
    values = []
    while True:
        user_input = input("Enter a value: ")
        if user_input == "":
            break
        values.append(user_input)
    print("Here's the list:", values)

collect_values()

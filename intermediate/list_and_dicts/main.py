def access_element(lst, index):
    if 0 <= index < len(lst):
        return lst[index]
    return "Index out of range"

def modify_element(lst, index, new_value):
    if 0 <= index < len(lst):
        lst[index] = new_value
        return "Element updated successfully"
    return "Index out of range"

def slice_list(lst, start, end):
    return lst[start:end]

def list_game():
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    while True:
        print("\nCurrent List:", fruit_list)
        choice = input("Choose an action - access, modify, slice, or quit: ").strip().lower()
        
        if choice == "access":
            index = int(input("Enter index to access: "))
            print("Result:", access_element(fruit_list, index))
        
        elif choice == "modify":
            index = int(input("Enter index to modify: "))
            new_value = input("Enter new value: ")
            print("Result:", modify_element(fruit_list, index, new_value))
        
        elif choice == "slice":
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print("Sliced List:", slice_list(fruit_list, start, end))
        
        elif choice == "quit":
            print("Game Over!")
            break
        else:
            print("Invalid choice! Try again.")

list_game()

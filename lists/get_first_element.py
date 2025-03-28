def get_first_element(lst):
    print(lst[0])

def main():
    lst = []
    while True:
        element = input("Enter an element (or 'done' to finish): ")
        if element == 'done':
            if lst:  # Check if list is not empty
                get_first_element(lst)
                break
            else:
                print("Please enter at least one element.")
        else:
            lst.append(element)

main()
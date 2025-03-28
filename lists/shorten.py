MAX_LENGTH = 3

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()
        print(removed_item)

def main():
    test_list = [1, 2, 3, 4, 5]
    shorten(test_list)
    print("Final list:", test_list)

main()

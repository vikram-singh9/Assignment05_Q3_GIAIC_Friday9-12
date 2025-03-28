def count_even(lst):
    while True:
        response = input("Enter an integer or press enter to stop: ")
        if response == "":
            break
        lst.append(int(response))
    
    even_count = 0
    for num in lst:
        if num % 2 == 0:
            even_count += 1
    print(even_count)

my_list = []
count_even(my_list)

if __name__ == '__main__':
    count_even(my_list)
def num_in_stock(fruit):
    pass

def main():
    fruit = input("Enter a fruit: ")
    count = num_in_stock(fruit)
    if count == 0:
        print("This fruit is not in stock.")
    elif count == 1:
        print("There is 1 fruit in stock.")
    elif count > 1:
        print(f"There are {count} fruits in stock.")
    

if __name__ == '__main__':
    main()
def num_in_stock(fruit):
    pass

def main():
    fruit = input("Enter a fruit: ")
    count = num_in_stock(fruit)
    if count > 0:
        print(count)
    else:
        print("This fruit is not in stock.")

main()
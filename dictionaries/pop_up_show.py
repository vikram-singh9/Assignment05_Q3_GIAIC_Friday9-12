def main():
    fruits = {"strawberry":5, "banana":3.2, "apple":2, "orange":4.2, "grape":1, "kiwi":6, "watermelon":7}
    total = 0
    for fruit in fruits:
        price = fruits[fruit]
        amount_bought = int(input(f"how many {fruit}s do want to buy?"))
        total += (price * amount_bought)
    print(f"Your total cost of all fruits is {total}PKR")


if __name__ == '__main__':  
    main()


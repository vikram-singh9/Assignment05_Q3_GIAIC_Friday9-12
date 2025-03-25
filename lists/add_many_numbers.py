def sum_of_numbers(numbers):
    total = 0  # Shuru mein sum zero se start karenge
    for num in numbers:  # Har number ko list se lenge
        total = total + num  # Total mein add karte jayenge
    return total  # Last mein total return karenge

# Test karne ke liye
my_list = [1, 2, 3, 4]
result = sum_of_numbers(my_list)
print(f"Sum of {my_list} is: {result}")
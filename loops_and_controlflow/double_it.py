MAX_VALUE = 10000

def fibonacci_up_to_max():
    a, b = 0, 1
    while a < MAX_VALUE:
        print(a)
        a, b = b, a + b

if __name__ == '__main__':
    fibonacci_up_to_max() 
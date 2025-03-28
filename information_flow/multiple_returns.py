def get_user_data():
    first = input("What is your first name?: ")
    last = input("What is your last name?: ")
    email = input("What is your email address?: ")
    return first, last, email

if __name__ == '__main__':
    first_name, last_name, email_address = get_user_data()
    print(f"Hello {first_name} {last_name}, your email address is {email_address}.")
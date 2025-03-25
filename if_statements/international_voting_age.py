brazil = 17
india  = 20
pakistan = 18

def main():
    user_age = int(input("Enter your age: ") )   
    if user_age >= brazil:
        print(f"You CAN vote in brazil where voting age is {brazil}")
    else:
        print(f"You can not vote in brazil where voting age is {brazil}")
    
    if user_age >= india:
        print(f"You CAN vote in india where voting age is {india}")
    else:
        print(f"You can not vote in india where voting age is {india}")


    if user_age >= pakistan:
        print(f"You CAN vote in pakistan where voting age is {pakistan}")   
    else:
        print(f"You can not vote in pakistan where voting age is {pakistan}")
   
if __name__ == '__main__':
    main()
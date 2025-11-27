
def multiplication_table():
    
    user_input = int(input("Enter a number to generate its multiplication table: "))
    limit = int(input("Enter the limit up to which you want the table to be generated: "))
    
    print(f"Multiplication Table of {user_input} up to {limit}: ")
    
    for i in range(1, limit + 1):
        print(f"{user_input} x {i} = {user_input * i}")

def digit_counter():
    user_input = int(input("Enter a integer to count its digits: "))
    
    count = 0
    
    if user_input == 0:
        count = 1
    else:
        while user_input != 0:
            user_input //= 10
            count += 1
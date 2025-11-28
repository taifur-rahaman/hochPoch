
def multiplication_table():
    user_input = int(input("Enter a number to generate its multiplication table: "))
    limit = int(input("Enter the limit up to which you want the table to be generated: "))
    
    print(f"Multiplication Table of {user_input} up to {limit}: ")
    
    for i in range(1, limit + 1):
        print(f"{user_input} x {i} = {user_input * i}")

def digit_counter():
    user_input = int(input("Enter a integer to count its digits: "))
    temp_input = user_input
    count = 0
    
    if user_input == 0:
        count = 1
    else:
        while user_input != 0:
            user_input //= 10
            count += 1
    print(f"The number of digits in {temp_input} is {count}.")

def sum_of_digits():
    user_input = int(input("Enter an integer to find the sum of its digits: "))
    temp_input = user_input
    total = 0
    while user_input != 0:
        digit = user_input % 10
        total += digit
        user_input //= 10
    print(f"The sum of the digits in {temp_input} is {total}.")

def reverse_digits():
    user_input = int(input("Enter an integer to reverse its digits: "))
    temp_input = user_input
    
    reversed_number = 0
    
    while user_input != 0:
        digit = user_input % 10
        reversed_number = reversed_number * 10 + digit
        user_input //= 10
    print(f"The reverse of the digits in {temp_input} is {reversed_number}.")

def min_max_finder():
    limit = int(input("Enter how many numbers you want to input: "))
    numbers = []
    
    for user_input in range(limit):
        num = float(input(f"Enter number {user_input + 1}: "))
        numbers.append(num)
        
    min = numbers[0]
    max = numbers[0]
    
    for num in numbers:
        if num < min:
            min = num
        if num > max:
            max = num
    print(f"The minimum number is : {min}\nThe maximum number is : {max}")

def factorial_of_number():
    user_input = int(input("Enter a non-negative integer to find its factorial: "))
    
    fact = 1
    
    for i in range(1, user_input + 1, 1):
        fact = fact * i
    
    print(f"The factorial is: {fact}")

def fabonacci_series():
    limit = int(input("Enter the number of terms for Fabonacci Series: "))
    series = [0, 1]
    for i in range(2, limit):
        next_term = series[i - 1] + series[i - 2]
        series.append(next_term)
    
    print(f"Fabonacci Series up to {limit} are: ")
    for i in range(limit):
        print(series[i], end=" ")

def asking_for_range():
    lower_limit = int(input("Enter the lower limit of the range: "))
    upper_limit = int(input("Enter the upper limit of the range: "))
    return lower_limit, upper_limit

def prime_range():
    lower, upper = asking_for_range()
    print(f"Prime numbers between {lower} and {upper} are: ")
    
    for number in range(lower, upper + 1):
        isPrime = True
        if number > 1:
            for i in range(2, int(number)):
                if (number % i) == 0:
                    isPrime = False
                    break
            if isPrime:
                print(number, end="\n")

def even_range():
    lower, upper = asking_for_range()
    for number in range(lower, upper + 1):
        if number % 2 == 0:
            print(number, end="\n")

def odd_range():
    lower, upper = asking_for_range()
    for number in range(lower, upper + 1):
        if number % 2 != 0:
            print(number, end="\n")
import rangeFinder, functionalities as func


print("Hochpoch Problems")

while True:
    choice = input("\nChoose an option:\n1. Multiplication Table\n2. Digit Counter\n3. Sum of Digits\n4. Reverse Digits\n5. In Range finder\n6. Minimum and Maximum Finder\n7. Factorial of Number\n8. Fabonacci Series\n0. Exit\nEnter Your Choice: ")
    
    if choice == "1":
        func.multiplication_table()
    elif choice == "2":
        func.digit_counter()
    elif choice == "3":
        func.sum_of_digits()
    elif choice == "4":
        func.reverse_digits()
    elif choice == "5":
        rangeFinder.choice()
    elif choice == "6":
        func.min_max_finder()
    elif choice == "7":
        func.factorial_of_number()
    elif choice == "8":
        func.fabonacci_series()
    elif choice == "0":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")
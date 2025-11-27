import rangeFinder, functionalities as func


print("Hochpoch Problems")

while True:
    choice = input("Choose an option:\n1. Multiplication Table\n2. Digit Counter\n3. Sum of Digits\n4. Reverse Digits\n5. In Range finder\n0. Exit\nEnter Your Choice: ")
    
    if choice == "1":
        func.multiplication_table()
    elif choice == "2":
        func.digit_counter()
    elif choice == "3":
        pass # Sum of Digits Code goes here
    elif choice == "4":
        pass # Reverse Digits Code goes here
    elif choice == "5":
        rangeFinder.choice()
    elif choice == "0":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")
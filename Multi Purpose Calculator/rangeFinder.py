import functionalities as func

def choice():
    print("In Range Finder\n")

    while True:
        choice = input("1. Prime Numbers\n2. Even Numbers\n3. Odd Numbers\n0. Return to Main Menu\nEnter Your Choice: ")
        
        if choice == "1":
            func.prime_range()
        elif choice == "2":
            func.even_range()
        elif choice == "3":
            func.odd_range()
        elif choice == "0":
            print("Returning to Main Menu.\n")
            break
        else:
            print("Invalid choice. Please try again.\n")
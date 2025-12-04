import defination

print("Area of Different Geometric Shapes")

while True:
    print("Choose the shape to Calculate Area:\n1. Square\n2. Rectangle\n3. Circle\n4. Triangle\n5. Trapezium\n6. Parallelogram\n0. Exit")
    
    choice = input("Enter your choice: ")
    
    match choice:
        case '1':
            defination.area_of_square()
        case '2':
            defination.area_of_rectangle()
        case '3':
            defination.area_of_circle()
        case '4':
            defination.area_of_triangle()
        case '5':
            defination.area_of_trapezium()
        case '6':
            defination.area_of_parallelogram()
        case '0':
            print("Exiting the program.")
            break
        case _:
            print("Invalid choice. Please try again.")
import math

def area_of_square():
    side = float(input("Enter the side length of the square: "))
    print(f"The area of the square is: {side * side}")

def area_of_rectangle():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    print(f"The area of the rectangle is: {length * width}")

def area_of_circle():
    radius = float(input("Enter the radius of the circle: "))
    print(f"The area of the circle is: {math.pi * radius * radius}")

def area_of_triangle():
    base = float(input("Enter the base length of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    print(f"The area of the triangle is: {0.5 * base * height}")

def area_of_trapezium():
    a = float(input("Enter the length of the first parallel side of the trapezium: "))
    b = float(input("Enter the length of the second parallel side of the trapezium: "))
    height = float(input("Enter the height of the trapezium: "))
    print(f"The area of the trapezium is: {0.5 * (a + b) * height}")

def area_of_parallelogram():
    base = float(input("Enter the base length of the parallelogram: "))
    height = float(input("Enter the height of the parallelogram: "))
    print(f"The area of the parallelogram is: {base * height}")


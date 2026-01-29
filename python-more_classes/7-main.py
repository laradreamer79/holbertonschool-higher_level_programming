#!/usr/bin/python3
Rectangle = __import__('7-rectangle').Rectangle

my_rectangle_1 = Rectangle(2, 3)
print(my_rectangle_1)

print("--")

Rectangle.print_symbol = "*"
my_rectangle_2 = Rectangle(2, 3)
print(my_rectangle_2)

print("--")

my_rectangle_3 = Rectangle(2, 3)
my_rectangle_3.print_symbol = "X"
print(my_rectangle_3)

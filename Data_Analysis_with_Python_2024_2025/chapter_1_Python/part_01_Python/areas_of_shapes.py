#!/usr/bin/env python3

import math


def main():
    while True:
        shape_choice = str(input("Choose a shape (triangle, rectangle, circle) :"))
        if shape_choice == "":
            break
        if shape_choice == "triangle":
            triangle_base = float(input("Give base of the triangle: "))
            triangle_height = float(input("Give height of the triangle: "))
            triangle_area = (1/2)*((triangle_base)*(triangle_height))
            print(f"The area is {triangle_area: .6f}")
        elif shape_choice == "rectangle":
            rectangle_width = float(input("Give width of the rectangle: "))
            rectangle_height = float(input("Give height of the rectangle: "))
            rec_area = rectangle_width * rectangle_height
            print(f"The area is {rec_area: .6f}")
        elif shape_choice == "circle":
            circle_radius = float(input("Give radius of circle"))
            circ_area = (math.pi)*((circle_radius)**2)
            print(f"The area is {circ_area: .6f}")
        else:
             print("Unknown shape!")
if __name__ == "__main__":
    main()

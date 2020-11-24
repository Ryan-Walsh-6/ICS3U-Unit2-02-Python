#!/usr/bin/env python3

# created by: Ryan Walsh
# created on: November 2020
# this program finds area and perimeter of a rectangle
import math


def main():
    # this program finds area and perimeter of a rectangle

    # input
    length = int(input("Enter the length of a rectangle (cm) :"))
    width = int(input("Enter the width of a rectangle (cm) :"))

    # process
    area = ((length)*(width))
    perimeter = (2*(length+width))

    # output
    print()
    print("Area is {} cm².".format(area))
    print("Perimeter is {} cm.".format(perimeter))


if __name__ == "__main__":
    main()

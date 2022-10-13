#!/usr/bin/env python3

# Created by: Lucas LeBlanc
# Created on: Oct 2022
# This program calculates addition of two numbers
#    with numbers inputted from the user


def main():
    # this function calculates addition

    # input
    number_1 = int(input("Enter first number to add (integer): "))
    number_2 = int(input("Enter second number to add (integer): "))

    # process
    sum = number_1 + number_2

    # output
    print("")
    print("{0} + {1} = {2}".format(number_1, number_2, sum))

    print("\nDone.")


if __name__ == "__main__":
    main()

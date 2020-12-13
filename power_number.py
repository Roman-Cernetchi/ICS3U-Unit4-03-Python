#!/usr/bin/env python3
#
# Created by: Roman Cernetchi
# Created on: December 2020
# This program finds the power of a number


def main():
    # This function calculates the power of a number

    # Input
    positive_integer_string = input("Enter the positive integer you chose: ")
    print("")

    # process
    try:
        positive_integer = int(positive_integer_string)

        assert positive_integer >= 0

        for loop_counter in range(positive_integer + 1):
            number_sum = loop_counter ** 2
            print("{}^2 = {}".format(loop_counter, number_sum))

    except AssertionError:
        print("Integer wasn't positive")
    except Exception:
        print("This was not an integer")


if __name__ == "__main__":
    main()

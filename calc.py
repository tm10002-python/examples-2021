""" Basic calculation. """
import math


def add(lh, rh):
    """ Add function. """
    return lh + rh


def subtract(lh, rh):
    """ Subtract function. """
    return lh - rh


def multiply(lh, rh):
    """ Multiply function. """
    return lh * rh


def divide(numerator, denominator):
    """ Divide function. """
    return numerator / denominator


if __name__ == "__main__":
    print(f"1 + 3 = {add(1, 3)}")
    print(f"4 - 1 = {subtract(4, 1)}")
    print(f"2 * 3 = {multiply(2, 3)}")
    print(f"3 / 2 = {divide(3, 2)}")

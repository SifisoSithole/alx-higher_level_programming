#!/usr/bin/env python3
def print_last_digit(number):
    lstDigit = abs(number) % 10
    print(lstDigit, end='')
    return lstDigit

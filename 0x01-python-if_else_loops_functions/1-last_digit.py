#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = number % 10
if number < 0:
    lastDigit *= -1
if lastDigit > 5:
    msg = "and is greater than 5"
elif lastDigit == 0:
    msg = "and is 0"
else:
    msg = "and is less than 6 and not 0"
print(f"Last digit of {number} is {lastDigit} {msg}")

#!/usr/bin/python3
def fizzbuzz():
    mulThree = 3
    mulFive = 5
    for i in range(1, 101):
        if i == mulThree and i == mulFive:
            print("FizzBuzz", end=" ")
            mulThree += 3
            mulFive += 5
        elif i == mulThree:
            print("Fizz", end=" ")
            mulThree += 3
        elif i == mulFive:
            print("Buzz", end=" ")
            mulFive += 5
        else:
            print(i, end=" ")

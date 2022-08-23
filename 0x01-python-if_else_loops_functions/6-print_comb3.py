#!/usr/bin/python3
for first in range(0,9):
    for second in range(first + 1, 10):
        if first != 8:
            print(f"{first}{second}", end=", ")
        else:
            print(f"{first}{second}")

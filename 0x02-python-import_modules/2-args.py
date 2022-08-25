#!/usr/bin/python3
import sys
if __name__ == "__main__":
    ac = len(sys.argv)
    if ac > 1:
        print(f"{ac:d} arguments:")
        for i in range(1, ac):
            print(f"{i:d}: {sys.argv[i]:s}")
    else:
        print("0 arguments")


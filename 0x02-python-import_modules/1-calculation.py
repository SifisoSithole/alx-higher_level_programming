#!/usr/bin/python3
import calculator_1 as cal
a = 10
b = 5
signs = ["+", "-", "*", "/"]
functions = [cal.add, cal.sub, cal.mul, cal.div]
for i in range(len(functions)):
    print("{0:d} {1:s} {2:d} = {3:d}".format(a, signs[i], b, functions[i](a, b)))

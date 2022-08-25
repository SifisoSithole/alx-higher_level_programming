#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as cal
    a = 10
    b = 5
    signs = ["+", "-", "*", "/"]
    func = [cal.add, cal.sub, cal.mul, cal.div]
    for i in range(len(func)):
        print("{:d} {:s} {:d} = {:d}".format(a, signs[i], b, func[i](a, b)))

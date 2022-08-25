#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as cal
    from sys import argv

    ac = len(argv)
    if ac != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        quit(1)
    a = int(argv[1])
    b = int(argv[3])
    signs = ["+", "-", "*", "/"]
    func = [cal.add, cal.sub, cal.mul, cal.div]
    for i in range(len(func)):
        if argv[2] == signs[i]:
            print("{:d} {:s} {:d} = {:d}".format(a, signs[i], b, func[i](a, b)))
            quit()
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        quit(1)

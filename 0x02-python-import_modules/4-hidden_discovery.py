#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    attributes = dir(hidden_4)
    for attribute in attributes:
        if attribute[0:2] != "__":
            print(attribute)

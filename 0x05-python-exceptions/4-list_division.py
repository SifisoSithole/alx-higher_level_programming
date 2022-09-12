#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            ans = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            ans = 0
            print("division by 0")
        except TypeError:
            ans = 0
            print("wrong type")
        except IndexError:
            print("out of range")
            ans = 0
        finally:
            result.append(ans)
    return result

#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_div_list = []
    for i in range(list_length):
        try:
            res = 0
            res = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except (TypeError, ValueError):
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            new_div_list.append(res)
    return new_div_list

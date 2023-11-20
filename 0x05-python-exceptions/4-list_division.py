#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for q in range(list_length):
        try:
            result.append(my_list_1[q] / my_list_2[q])
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except (TypeError, ValueError):
            print("Wrong type")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
        finally:
            pass
    return (result)    


from math import *


def calculator():
    print()
    print('pi =', pi)
    while True:
        print()
        cal = input('DO YOUR OPERATION DIRECTLY: ').lower()
        if cal == 'exit' or cal == 'close':
            break
        else:
            print()
            cal2 = eval(cal)
            print(cal2)
            return cal2

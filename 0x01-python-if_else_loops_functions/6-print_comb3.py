#!/usr/bin/python3
num = 0
while num <= 89:
    tens_digit = num // 10
    ones_digit = num % 10
    if tens_digit != ones_digit:
        if num < 89:
            print("{:02d}, ".format(num), end='')
        else:
            print("{:02d}".format(num))
            num += 1

#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a, op, b = sys.argv[1:4]
    if op not in ('+', '-', '*', '/'):
         print("Unknown operator. Available operators: +, -, *, and /")
         sys.exit(1)
    a, b = int(a), int(b)     
    operators = {
             '+': add,
             '-': sub,
             '*': mul,
             '/': div,
             }
    if b == 0 and (op in ('/', '%')):
         print("Error: dividion by zero")
         sys.exit(1)
    result = operators[op](a, b)
    print(f"{a} {op} {b} = {result}")

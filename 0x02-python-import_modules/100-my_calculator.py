#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    oper = sys.argv[2]
    if oper != "+" and oper != "-" and oper != "*" and oper != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    calc = 0
    num1 = sys.argv[1]
    num2 = sys.argv[3]
    num_args = len(sys.argv)
    for i in range(1, num_args):
        calc += int(sys.argv[i])
    print("{} {} {} = {}".format(num1, oper, num2, calc))    

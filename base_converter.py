"""
This script asks the user for two numbers: a and b; then it convert a into base b.
It require both a and b are integer with a > 0 and  1 < b < 11.
"""

a = int(input("input your number: "))
b = int(input("Convert %s to base: "%a))

def divide(divisor, dividend):
    quotient  = divisor // dividend
    remainder = divisor %  dividend
    return (quotient, remainder)

def convert(number, base):
    list_remainder = ""
    quotient, remainder = divide(number, base)
    list_remainder += str(remainder)
    while quotient != 0:
        quotient, remainder = divide(quotient, base)
        list_remainder += str(remainder)
    return "".join(reversed(list_remainder))

print(convert(a, b))

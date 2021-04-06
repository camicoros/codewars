"""
Reverse polish notation calculator
link: https://www.codewars.com/kata/52f78966747862fc9a0009ae/train/python
Your job is to create a calculator which evaluates expressions 
in Reverse Polish notation.

For example 
expression 5 1 2 + 4 * + 3 - (which is equivalent to 5 + ((1 + 2) * 4) - 3 
in normal notation) should evaluate to 14.

For your convenience, the input is formatted such that a space 
is provided between every token.

Empty expression should evaluate to 0.

Valid operations are +, -, *, /.

You may assume that there won't be exceptional situations 
(like stack underflow or division by zero).
"""


def calc(expr):
    result = 0
    if expr == '':
        return result
    try:
        result = float(expr.strip())
    except:
        sign = expr[-1]
        last_space = expr[:-2].rfind(' ')
        if expr[-3] in ('+', '-', '*', '/'):
            first, second = expr.split(' ', 1)
            second = second[:-2]
        else:
            first = expr[:last_space]
            second = expr[last_space:-2]
        
        if sign == '+':
             result = calc(first) + calc(second)
        if sign == '-':
             result = calc(first) - calc(second)
        if sign == '/':
             result = calc(first) / calc(second)
        if sign == '*':
            result = calc(first) * calc(second)
        
    return result


def main():
    print(calc(""), 0, "Should work with empty string")
    print(calc("3"), 3, "Should parse numbers")
    print(calc("3.5"), 3.5, "Should parse float numbers")
    print(calc("1 3 +"), 4, "Should support addition")
    print(calc("1 3 *"), 3, "Should support multiplication")
    print(calc("1 3 -"), -2, "Should support subtraction")
    print(calc("4 2 /"), 2, "Should support division")
    print(calc("5 1 2 + 4 * + 3 -"), 14, "Should work with complicated expressions")


if __name__ == "__main__":
    main()

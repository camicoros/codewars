"""
Given n, take the sum of the digits of n. 
If that value has more than one digit, 
continue reducing in this way until a single-digit number is produced. 
The input will be a non-negative integer.

Examples
    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
"""


def digital_root(n):
    end = False
    while not end:
      result = 0
      while n > 0:
        result += n%10
        n = n // 10
      n = result
      if n < 10:
        end = True
    return n

def digital_root_with_str(n):
    end = False
    while not end:
        result = 0
        for i in str(n):
            result += int(i)
        n = result
        if n < 10:
            end = True
    return n
  
def main():
    print(digital_root(493193))

if__name __ == «__main__»:
    main()

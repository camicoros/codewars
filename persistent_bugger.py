"""
Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, 
which is the number of times you must multiply the digits in num until you reach a single digit.

For example:

persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
                       # and 4 has only one digit.
                 
persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
                       # 1*2*6 = 12, and finally 1*2 = 2.
                  
persistence(4) => 0   # Because 4 is already a one-digit number.
"""

def persistence(n):
    finish = False
    counter = 0
    
    while not finish:
        if n < 10:
            finish = True
            continue

        new_n = n % 10
        while n // 10 > 0:
            n = n // 10
            new_n *= (n % 10)

        n = new_n
        counter += 1

    return counter

def main():
    persistence(39)

if __name__ == "__main__":
    main()

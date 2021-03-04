"""
Write a function, which takes a non-negative integer (seconds) 
as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.
"""


def make_readable(seconds):
    my_seconds = seconds % 60
    seconds = seconds // 60
    minutes = seconds % 60
    seconds = seconds // 60
    hours = seconds % 100
    return "{:02d}:{:02d}:{:02d}".format(hours, minutes, my_seconds)


def main():
    print(make_readable(0))
    print(make_readable(5))
    print(make_readable(60))
    print(make_readable(86399))
    print(make_readable(359999))

if __name__ == "__main__":
    main()

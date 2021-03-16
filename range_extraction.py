"""
Range Extraction
link: https://www.codewars.com/kata/51ba717bb08c1cd60f00002f
A format for expressing an ordered list of integers is to use a comma separated list of either

individual integers
or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. 
The range includes all integers in the interval including both endpoints. 
It is not considered a range unless it spans at least 3 numbers. 
For example "12,13,15-17"
Complete the solution so that it takes a list of integers in increasing order and 
returns a correctly formatted string in the range format.

Example:

solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-6,-3-1,3-5,7-11,14,15,17-20"
"""


def solution(args):
    result_list = []
    current_list = []
    for num, i in enumerate(args[:-1]):
        if current_list:
            if args[num + 1] == i + 1:
                current_list.append(i)
            else:
                current_list.append(i)
                for j in compress(current_list):
                    result_list.append(str(j))
                current_list = []
        else:
            if args[num + 1] == i + 1:
                current_list.append(i)
            else:
                result_list.append(str(i))

    if args:
        current_list.append(args[-1])
        for i in compress(current_list):
            result_list.append(str(i))
    return ','.join(result_list)


def compress(args):
    if len(args) <= 2:
        return args
    else:
        return [
            "{}-{}".format(args[0], args[-1]),
        ]


def main():
    print(
      solution([
          -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20
      ])
    )
    print(solution([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20]))


if __name__ == "__main__":
    main()

"""
Snail Sort
link: https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1
Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]

NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].
"""


def snail(snail_map):
    print("__snail_start__")
    snail_len = len(snail_map[0])

    current_i = 0
    current_j = 0

    result_list = []

    iteration_len = snail_len

    current_action = 0

    while iteration_len > 0:
        if iteration_len == snail_len:
            counter = 1
        else:
            counter = 2
        while counter > 0:
            counter -= 1

            if current_action == 0:
                print('right {} from {}{} to {}{}'.format(iteration_len,
                                                          current_i,
                                                          current_j,
                                                          current_i,
                                                          current_j + iteration_len - 1,
                                                          ))
                iterations = current_j + iteration_len - 1
                while current_j <= iterations:
                    result_list.append(snail_map[current_i][current_j])
                    current_j += 1
                current_i += 1
                current_j -= 1

            elif current_action == 1:
                print('down {} from {}{} to {}{}'.format(iteration_len,
                                                         current_i,
                                                         current_j,
                                                         current_i + iteration_len - 1,
                                                         current_j,
                                                         ))
                iterations = current_i + iteration_len - 1
                while current_i <= iterations:
                    result_list.append(snail_map[current_i][current_j])
                    current_i += 1
                current_i -= 1
                current_j -= 1

            elif current_action == 2:
                print('left {} from {}{} to {}{}'.format(iteration_len,
                                                         current_i,
                                                         current_j,
                                                         current_i,
                                                         abs(current_j - iteration_len + 1),
                                                         ))
                iterations = abs(current_j - iteration_len + 1)
                while current_j >= iterations:
                    result_list.append(snail_map[current_i][current_j])
                    current_j -= 1
                current_i -= 1
                current_j += 1

            elif current_action == 3:
                print('up {} from {}{} to {}{}'.format(iteration_len,
                                                       current_i,
                                                       current_j,
                                                       abs(current_i - iteration_len + 1),
                                                       current_j,
                                                       ))
                iterations = abs(current_i - iteration_len + 1)
                while current_i >= iterations:
                    result_list.append(snail_map[current_i][current_j])
                    current_i -= 1
                current_i += 1
                current_j += 1

            current_action = (current_action + 1) % 4

        iteration_len -= 1
         
    print(result_list)     
    print("__snail_end__\n")
    return result_list


def main():
    array = [[1, 2],
             [4, 5]]
    snail(array)

    array = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
    snail(array)

    array = [[1, 2, 3],
             [8, 9, 4],
             [7, 6, 5]]
    snail(array)

    array = [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12],
             [13, 14, 15, 16]]
    snail(array)

    array = [[1, 2, 3, 4, 5],
             [6, 7, 8, 9, 10],
             [11, 12, 13, 14, 15],
             [16, 17, 18, 19, 20],
             [21, 22, 23, 24, 25]]
    snail(array)


if __name__ == "__main__":
    main()

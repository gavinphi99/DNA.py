#  File: DNA.py

#  Description: A program that finds the longest common substring(s) of two strings and prints them out

#  Student Name: Phillip Gavino

#  Student UT EID: pag2529

#  Partner Name: Jack Qiao

#  Partner UT EID: jq3838

#  Course Name: CS 313E

#  Unique Number: 52590

#  Date Created: 8/24/2021

#  Date Last Modified: 8/27/2021

# Input: s1 and s2 are two strings that represent strands of DNA
# Output: returns a sorted list of substrings that are the longest
#         common subsequence. The list is empty if there are no
#         common subsequences.

#       1   2   3   4   5   6   7   8   9   10  11  12  13
#       G   T   G   A   T   A   A   G   G   A   C   C   C
#  1 A [0,  0,  0,  1,  0,  1,  1,  0,  0,  1,  0,  0,  0]
#  2 T [0,  1,  0,  0,  2,  0,  0,  0,  0,  0,  0,  0,  0]
#  3 G [1,  0,  2,  0,  0,  0,  0,  1,  1,  0,  0,  0,  0]
#  4 A [0,  0,  0,  3,  0,  1,  1,  0,  0,  2,  0,  0,  0]
#  5 T [0,  1,  0,  0,  4,  0,  0,  0,  0,  0,  0,  0,  0]
#  6 G [1,  0,  2,  0,  0,  0,  0,  1,  1,  0,  0,  0,  0]
#  7 G [1,  0,  1,  0,  0,  0,  0,  1,  2,  0,  0,  0,  0]
#  8 A [0,  0,  0,  2,  0,  1,  1,  0,  0,  3,  0,  0,  0]
#  9 C [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  4,  1,  1]

import sys


def longest_subsequence(s1, s2):

    m, n = len(s1), len(s2)  # m x n matrix
    string_matrix = [[0 for k in range(n + 1)] for l in range(m + 1)]  # creates matrix
    len_long_lcs = 0  # length of longest common substring found so far
    temp = []
    answer = []

    for i in range(m):
        for j in range(n):
            if (s1[i - 1] == s2[j - 1]):  # as shown in the above diagram, must see if the cell diagonally left is equal
                string_matrix[i][j] = string_matrix[i - 1][j - 1] + 1  # if it is equal then the new cell value is
                # equal to the old one plus 1

                if (string_matrix[i][j] > len_long_lcs):  # if the cell number is greater than the length of the
                    # longest common substring found so far
                    len_long_lcs = string_matrix[i][j]  # then the longest common substring becomes the cell number

            if (len_long_lcs == string_matrix[i][j]):
                end_index = i
                temp.append(s1[end_index - len_long_lcs: end_index])

    max_length = None
    for x in temp:
        if (max_length is None or len(x) > max_length):
            max_length = len(x)

    for y in temp:
        if (y == ''):
            answer = []
        elif (len(y) == max_length):
            answer.append(y)

    return sorted(answer)


def main():
    pairs = []
    n = sys.stdin.readline()
    lines = sys.stdin.readlines()

    for i in range(len(lines)):
        if (i % 2 == 1):
            s1 = lines[i - 1]  # first of the pair
            s2 = lines[i]  # second of the pair
            s1.upper()
            s2.upper()
            pairs.append(longest_subsequence(s1, s2))

    for x in pairs:
        print()
        if x:  # if there is a list element
            for y in x:  # loop through list elements of the lists
                print(y)
        else:
            print("No Common Sequence Found")


if __name__ == "__main__":
    main()

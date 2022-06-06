"""
sample array:
value: -40 -20   -1     1     2    3    5     7     9      12    13
index:  0   1     2     3     4    5    6     7     8      9     10

magic index is 7 since array[7] = 7

Magic Index: A magic index in an array A [ 0••• n -1] is defined to be an index such that A[ i] =
i. Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in
array A.
FOLLOW UP
What if the values are not distinct?
"""

def magicIndexBruteForce(array):
    
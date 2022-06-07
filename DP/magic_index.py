"""
sample array:
value: -40    -20    -1     1     2     3     5     7     9      12    13
index:  0      1      2     3     4     5     6     7     8      9     10

magic index is 7 since array[7] = 7

Magic Index: A magic index in an array A [ 0••• n -1] is defined to be an index such that A[ i] =
i. Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in
array A.
FOLLOW UP
What if the values are not distinct?
"""
import math
from turtle import right

def magicIndexBruteForce(array):
    magicIndex = []
    for i in range(len(array)):
        if i == array[i]:
            magicIndex.append(i)

    return magicIndex

# This is for unique values only
import math
def magicIndexRecursiveUnique(array, index=0):
    if len(array) == 1:
        if array[0] == index:
            return array

    else:
        
        left_result = magicIndexRecursiveUnique(array[:math.floor(len(array)/2)],index)
        right_result = magicIndexRecursiveUnique(array[math.floor(len(array)/2):],index+math.floor(len(array)/2))

        if left_result != None:
            return left_result
        
        if right_result != None:
            return right_result

    return None

print(magicIndexRecursiveUnique([1,2,3,4,4,6,7]))
# print(magicIndexBruteForce([-40, -20,   -1,     1,     2,    3,    5,     7,     9,      12    ,13]))

# This is for duplicate values also
import math
def magicIndexRecursiveMultiple(array, index=0):
    all_results = []
    if len(array) == 1:
        if array[0] == index:
            return array

    else:
        index_temp = math.floor(len(array)/2)
        left_result_temp = magicIndexRecursiveMultiple(array[:index_temp], index)
        right_result_temp = magicIndexRecursiveMultiple(array[index_temp:], index + index_temp)

        if left_result_temp != None:
            all_results.extend(left_result_temp)
        
        if right_result_temp != None:
            all_results.extend(right_result_temp)

        if len(all_results) > 0:
            # print('returning all results')
            return all_results

    return None

magicIndexRecursiveMultiple([1,2,3,4,4,6,7])
# print(magicIndexBruteForce([-40, -20,   -1,     1,     2,    3,    5,     7,     9,      12    ,13]))



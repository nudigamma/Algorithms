import random
import argparse
import heapq

# pass the file name as an argument
parser = argparse.ArgumentParser(description='RSelect')
parser.add_argument('readFromFile', type=bool, help='Read from file or not')
parser.add_argument('file', type=str, help='file name')
parser.add_argument('ith', type=int, help='ith order statistic')

args = parser.parse_args()


def partition(array : list[int]) -> int:
    pivot_value = array[0]
    i = 1
    for j in range(1, len(array)): # range is exclusive
        if array[j] < pivot_value:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[0], array[i - 1] = array[i - 1], array[0]
    return i - 1

def RSelect(array : list[int], ith : int) -> int:   
    if len(array) == 1:
        return array[0]
    pivot_index = random.randint(0, len(array) - 1) # randint int is inclusive
    array[0], array[pivot_index] = array[pivot_index], array[0]
    j = partition(array)
    if j == ith:
        return array[j]
    elif j > ith:
        return RSelect(array[:j], ith) # skips the pivot element
    else:
        return RSelect(array[j + 1:], ith - j - 1) # skips the pivot element

# test the algorithm 
# read a text file that has an array with each element on a new line

if (args.readFromFile):
    file_path = args.file
    with open(file_path) as f:
        array = f.readlines()
        array = [int(x.strip()) for x in array]

#  finding the ith order statistic of the array using heapq
ith = args.ith 

array1 = array.copy()
assert( heapq.nsmallest(ith,array)[-1] == RSelect(array1, ith-1))
print(RSelect(array, ith - 1))
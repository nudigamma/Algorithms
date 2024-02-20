import random
import argparse

# pass the file name as an argument
parser = argparse.ArgumentParser(description='RSelect')
parser.add_argument('file', type=str, help='file name')
args = parser.parse_args()
def partition(array):
    pivot_value = array[0]
    i = 1
    for j in range(1, len(array)):
        if array[j] < pivot_value:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[0], array[i - 1] = array[i - 1], array[0]
    return i - 1

def Rselect(array, ith):
    if len(array) == 1:
        return array[0]
    pivot_index = random.randint(0, len(array) - 1)
    array[0], array[pivot_index] = array[pivot_index], array[0]
    j = partition(array)

    if j == ith:
        return array[j]
    elif j > ith:
        return Rselect(array[:j], ith)
    else:
        return Rselect(array[j + 1:], ith - j - 1)


# test the algorithm 
# read a text file that has an array with each element on a new line

file_path = args.file
with open(file_path) as f:
    array = f.readlines()
    array = [int(x.strip()) for x in array]
print(array)
#  finding the ith order statistic of the array using heapq
import heapq
ith = 5
print(heapq.nsmallest(ith,array)[-1])
array1 = array.copy()
print(Rselect(array1, ith - 1))

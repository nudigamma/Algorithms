import random
import argparse
import heapq
import statistics

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

def Dselect(array : list[int], ith : int) -> int:   
    if len(array) == 1:
        return array[0]
    C = []
    for h in range(0,len(array)//5):
        if(len(array[h*5:(h+1)*5]) < 5):
            C.append(statistics.median(array[h*5:(h+1)*5]))    
    p = Dselect(C,len(C)//2)
    index_p = array.index(p)
    array[0], array[index_p] = array[index_p], array[0]
    if j == ith:
        return array[j]
    elif j > ith:
        return Rselect(array[:j], ith) # skips the pivot element
    else:
        return Rselect(array[j + 1:], ith - j - 1) # skips the pivot element

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
assert( heapq.nsmallest(ith,array)[-1] == Rselect(array1, ith - 1))
print(Rselect(array, ith - 1))
'''This function implements the bubble sort algorithm.'''
import numpy as np 
import unittest
import sys
import platform
os_type = platform.system()
if os_type == 'Windows':
    sys.path.insert(0, r'D:\\source\\Algorithms\\')
    sys.path.insert(0, r'D:\\source\\Algorithms\\DataStructures\\')
elif os_type == 'Linux':
    sys.path.insert(0, r'/mnt/c/source/Algorithms-Iluminated/')
    sys.path.insert(0, r'/mnt/c/source/Algorithms-Iluminated/DataStructures')
import Utils.RandomDataGenerator as rnd

def swapelement(i,j):
    '''swaps the ith and jth element of the array'''
    temp = i
    i = j
    j = temp
    return i,j

def bubbleSort(array,verbose=False):
    '''input is an array of integers'''
    n = array.shape[0] # number of elements in the array
    swapped = True
    count = 0 
    start = 0
    end = n-1
    while (swapped) :
        
        for i in np.arange(start,end):
            if array[i] > array[i+1]:
                array[i],array[i+1] = swapelement(array[i],array[i+1])
                swapped = True
                count += 1
        if swapped == False:
            break
        swapped = False
        end = end - 1
        for i in np.arange(end-1,start-1,-1):
            if array[i] > array[i+1]:
                array[i],array[i+1] = swapelement(array[i],array[i+1])
                swapped = True
                count += 1
        start = start + 1
        if verbose:
            print(f"Bubble Sort array = {array}")    
    return array,count
class TestBubbleSort(unittest.TestCase):
    def test_bubble_sort(self):
        number_of_tests = 3000
        print(f"Generating {number_of_tests} tests \n")
        for i in range(number_of_tests):
            array =  rnd.generateRandomArray(1000,2000,0,10)
            sorted_array,count = bubbleSort(array)
            error = np.sort(array)-sorted_array
            assert error.all() == 0
        print(f"Completed {number_of_tests} tests \n")

if __name__ == '__main__':
    unittest.main()
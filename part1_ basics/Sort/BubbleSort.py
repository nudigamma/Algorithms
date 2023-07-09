'''This function implements the bubble sort algorithm.'''
import numpy as np 
import unittest
import sys 
sys.path.insert(0, r'D:\\source\\Algorithms-Iluminated\\part1_ basics')
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
            array = rnd.generateRandomArray(10,1000,-10000,10000)
            sorted_array,count = bubbleSort(array)
            error = np.sort(array)-sorted_array
            assert error.all() == 0
        print(f"Completed {number_of_tests} tests \n")

if __name__ == '__main__':
    unittest.main()
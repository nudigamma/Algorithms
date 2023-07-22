'''this program implements insertion sort from Introduction to Algorithms by Stein et al. @page 45'''
import numpy as np
import unittest
import sys
# get os type
import platform
os_type = platform.system()
if os_type == 'Windows':
    sys.path.insert(0, r'D:\\source\\Algorithms\\')
    sys.path.insert(0, r'D:\\source\\Algorithms\\DataStructures\\')
elif os_type == 'Linux':
    sys.path.insert(0, r'/mnt/c/source/Algorithms-Iluminated/')
    sys.path.insert(0, r'/mnt/c/source/Algorithms-Iluminated/DataStructures')
import Utils.RandomDataGenerator as rnd
import Lists.DoubleLinkedList as DList

def insertionSort_Array(array,step=False,verbose=False):
    '''input is an array of integers'''
    n = array.shape[0] # number of elements in the array
    count = 0
    for i in range(1,n):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key: #similar to bubble sort propagate the key to the left
            array[i] = array[j] #swap
            array[j] = key #swap 
            j = j - 1 # decrement j
            count += 1
            if verbose:
                print(f"Insertion Sort array = {array}")
            if step:
                input()
                print(f"Insertion Sort array = {array}")
        
    return array,count


class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort_array(self):
        number_of_tests = 3000
        print(f"Generating {number_of_tests} tests \n")
        for i in range(number_of_tests):
            print(f"Test {i+1} \n")
            array = rnd.generateRandomArray(10000,100000,0,10)
            error = np.sort(array)-insertionSort_Array(array)[0]
            assert error.all() == 0
        print(f"Completed {number_of_tests} tests \n")
    def test_insertion_sort_dlist(self):
        number_of_tests = 3000
        print(f"Generating {number_of_tests} tests \n")
        for i in range(number_of_tests):
            dlist = DList.LinkedNumber()
            array = rnd.generateRandomArray(1,20,0,10)
            for element in array:
                dlist.insert_at_beginning(element)
            dlist.insertionSort()
            error = np.sort(array)-dlist.to_array()
            assert error.all() == 0

if __name__ == '__main__':
    unittest.main()
 
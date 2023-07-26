'''This file implements the merge sort algorithm.'''

import numpy as np
import unittest
import sys
# get os type
import platform
os_type = platform.system()
if os_type == 'Windows':
    sys.path.insert(0, r'c:\\source\\Algorithms\\')
    sys.path.insert(0, r'c:\\source\\Algorithms\\DataStructures\\')
elif os_type == 'Linux':
    sys.path.insert(0, r'/mnt/d/source/Algorithms/')
    sys.path.insert(0, r'/mnt/d/source/Algorithms/DataStructures')  

#import Utils.RandomDataGenerator as rnd


def SecondLargest(array):
    if array.shape[0] == 1:
        return np.array([array[0],np.NINF])
    if array.shape[0] == 2:
        if array[0] > array[1]:
            return array
        else:
            temp = array[1]
            array[1] = array[0]
            array[0] = temp
            return array
    
    else:
        left  = SecondLargest(array[0:array.shape[0]//2])
        right  = SecondLargest(array[array.shape[0]//2:])
        

        if left[0] > right[0]:
            largest = left[0]
            if right [0] > left[1]:
                secondLargest = right[0]
            else:
                secondLargest = left[1]
        else :
            largest = right[0]
            if left[0] > right[1]:
                secondLargest = left[0]
            else:
                secondLargest = right[1]

        
        return np.array([largest,secondLargest])
    

    
class TestMergeSort(unittest.TestCase):
    def test_merge_sort(self):
        number_of_tests = 3000
        print(f"Generating {number_of_tests} tests \n")
        for i in range(number_of_tests):
            array = np.random.randint(0,10,10)
            error = np.sort(array)[-2] - SecondLargest(array)[1]
        assert error.all() == 0
        print(f"Completed {number_of_tests} tests \n")  

if __name__ == '__main__':
    unittest.main()
    #a = np.array([21,8,64,17,91,42,35,5])
    #SecondLargest(a)
    #print(SecondLargest(a)[1])
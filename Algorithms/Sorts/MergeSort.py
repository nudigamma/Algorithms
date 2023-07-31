'''This file implements the merge sort algorithm.'''

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

def mergeSort(array):
    c = np.zeros(array.shape[0])
    if array.shape[0] == 1:
        return array
    else:
        
        right = mergeSort(array[0:array.shape[0]//2])
        left = mergeSort(array[array.shape[0]//2:])
        i = 0
        j = 0
        k = 0

        while (i < right.shape[0]) and (j < left.shape[0]):
                if right[i] < left[j]:
                    c[k] = right[i]
                    i += 1
                else: 
                    c[k] = left[j] 
                    j += 1
                k += 1
        while i < right.shape[0]:
                c[k] = right[i]
                i += 1
                k += 1
        while j < left.shape[0]:
                c[k] = left[j]
                j += 1
                k += 1
        return c
    

    
class TestMergeSort(unittest.TestCase):
    def test_merge_sort(self):
        number_of_tests = 3000
        print(f"Generating {number_of_tests} tests \n")
        for i in range(number_of_tests):
            array = rnd.generateRandomArray(1000,2000,0,10)
            error = np.sort(array)-mergeSort(array)
        assert error.all() == 0
        print(f"Completed {number_of_tests} tests \n")  

if __name__ == '__main__':
    unittest.main()

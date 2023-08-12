'''This file implements the merge sort algorithm.'''

import numpy as np
import unittest
import sys
# get os type


    
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
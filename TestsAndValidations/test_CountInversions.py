'''This file implements the merge sort algorithm.'''

import numpy as np
import unittest
import sys
import socket 
import os
# get os type
import os 
import sys 
import platform

    

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
print(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import Utils.RandomDataGenerator as rnd
from Algorithms.CountInversions import bruteForeCountInversion, Sort_And_CountInV

class TestMergeSort(unittest.TestCase):
    def test_merge_sort(self):
        number_of_tests = 3000
        print(f"Generating {number_of_tests} tests \n")
        for i in range(number_of_tests):
            array = rnd.generateRandomArray(1000,2000,0,10)
            error = np.sort(array)-MergeSort(array)
        assert error.all() == 0
        print(f"Completed {number_of_tests} tests \n")  

if __name__ == '__main__':
    #unittest.main()
    array = np.array([6,5,4,3,2,1])
    output = np.zeros(array.shape[0])
    print(f"array = {array}")
    print(f"bruteForeCountInversion(array) = {bruteForeCountInversion(array)}")
    print(f"merge_and_CountSplit_Inv(array) = {Sort_And_CountInV(array)}")
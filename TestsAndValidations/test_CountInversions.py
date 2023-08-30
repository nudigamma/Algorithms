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

class TestCountInversion(unittest.TestCase):
    def test_count_inversion(self):
        print(f"Reading a text file with 28 inversions \n")
        array = np.loadtxt("CountInv100k.txt", dtype=int)
        #print(f"bruteForeCountInversion(array) = {bruteForeCountInversion(array)}")
        print(f"merge_and_CountSplit_Inv(array) = {Sort_And_CountInV(array)[1]}")
        assert Sort_And_CountInV(array)[1] == 2407905288
        

if __name__ == '__main__':
    unittest.main()
    #array = np.array([ 8, 7, 6, 5, 4, 3, 2, 1])
    #output = np.zeros(array.shape[0])
    #print(f"array = {array}")
    #print(f"bruteForeCountInversion(array) = {bruteForeCountInversion(array)}")
    #print(f"merge_and_CountSplit_Inv(array) = {Sort_And_CountInV(array)}")
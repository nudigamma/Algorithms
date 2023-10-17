'''This program tests the BinarySearch and RecursiveBinarySearc function in Algorithms/Search/Search.py '''
import unittest
#import the binarysearch function from ../Algorithms/Search/Search.py add the directory to the path
import sys
sys.path.append('../')

import sys
sys.path.append('/home/bandapear/Documents/source/Algorithms_and_Data_Structures/Algorithms/Search')
from Search import BinarySearch, BinarySearchRecursive

class TestBinarySearch(unittest.TestCase):
    #generate a random array 
    def setUp(self):
        self.array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    #test the binarysearch function
    def test_binarysearch(self):
        self.assertEqual(BinarySearch(self.array, 5), 4)
        self.assertEqual(BinarySearch(self.array, 1), 0)
        self.assertEqual(BinarySearch(self.array, 9), 8)
        self.assertEqual(BinarySearch(self.array, 10), -1)
        self.assertEqual(BinarySearch(self.array, 0), -1)

#main
if __name__ == '__main__':
    unittest.main()



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
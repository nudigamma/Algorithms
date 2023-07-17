'''this program implements insertion sort from Introduction to Algorithms by Stein et al. @page 45'''
import numpy as np
import unittest
import sys
# get os type
import platform
os_type = platform.system()
if os_type == 'Windows':
    sys.path.insert(0, r'D:\\source\\Algorithms\\')
elif os_type == 'Linux':
    sys.path.insert(0, r'/mnt/c/source/Algorithms-Iluminated/')
import Utils.RandomDataGenerator as rnd

def insertionSort(array,step=False,verbose=False):
    '''input is an array of integers'''
    n = array.shape[0] # number of elements in the array
    count = 0
    for i in range(1,n):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j+1] = array[j]
            j = j - 1
            array[j+1] = key
            count += 1
            if verbose:
                print(f"Insertion Sort array = {array}")
            if step:
                input()
                print(f"Insertion Sort array = {array}")
        
    return array,count

class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort(self):
        number_of_tests = 3000
        print(f"Generating {number_of_tests} tests \n")
        for i in range(number_of_tests):
            array = rnd.generateRandomArray(10,11,0,10)
            error = np.sort(array)-insertionSort(array,step=True)[0]
            assert error.all() == 0
        print(f"Completed {number_of_tests} tests \n")

if __name__ == '__main__':
    unittest.main()

'''This program implements the three sum algorithm and compares the running time of the brute force algorithm and the binary search algorithm.'''
import numpy as np
import os 
import sys
import platform as pl
if pl.system() == 'Windows':
    sys.path.insert(0,os.path.join('D:\\','source','Algorithms','Algorithms','Sort'))
    sys.path.insert(0,os.path.join('D:\\','source','Algorithms','Algorithms','Search'))
else:
    sys.path.insert(0,os.path.join(r'/mnt/d/source/Algorithms/Algorithms/Sort'))
    sys.path.insert(0,os.path.join(r'/mnt/d/source/Algorithms/Algorithms/Search'))


    

from Sort import MergeSort
from Search import BinarySearch

def ThreeSumBruteForce(inputArray):
    '''this function implements the three sum algorithm using the brute force method'''
    '''inputArray is a numpy array of integers'''
    '''this function returns the number of triplets that sum to zero'''

    count = 0
    for i in np.arange(inputArray.size):
        
        for j  in np.arange(i+1,inputArray.size):
             
            for z in np.arange(j+1,inputArray.size):
                
                if inputArray[i] + inputArray[j] + inputArray[z] == 0:
                    count +=1

    return count

def ThreeSumQuick(inputArray,SortFunction = MergeSort):
    '''this function implements the three sum algorithm using the binary search and sort'''
    ''' this function takes Sort function from Sort.py'''
    '''you can use your sort flavor from Sort.py'''
    '''inputArray is a numpy array of integers'''

    sortedArray = SortFunction(inputArray)
    count = 0
    for i in np.arange(sortedArray.size):
        for j in np.arange(i+1,sortedArray.size):
            if BinarySearch(sortedArray,-sortedArray[i]-sortedArray[j]) > j:
                count += 1
    return count

    
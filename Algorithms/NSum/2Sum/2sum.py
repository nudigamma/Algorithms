'''This program is written by Nadim Farhat as part of studying the Algorithm Book by Sedgewick and Wayne'''
'''We are going to implement two 2sum Algorithm , the brute force and the quick 2sum '''
'''We are going to compare the running time of both algorithms and see which one is faster'''
import numpy as np  # importing numpy library
import time as time  # importing time library
import sys 
import os
import platform

#use platfrom to check the operating system
if platform.system() == 'Linux':
    sort_module = os.path.join(r'/mnt/d/source/Algorithms_and_Data_Structures/Algorithms/Sorts')
if platform.system() == 'Windows':
    sort_module = os.path.join(r'D:\source\Algorithms_and_Data_Structures\Algorithms\Sorts')
        
sys.path.insert(0,sort_module)
from MergeSort import mergSort

array_sizes = np.array([1000, 2000, 4000, 8000, 16000, 32000, 64000])  # array of sizes

# creating a function that will generate random numbers


def binary_search_array(array, key):
    '''perform binary search on a sorted array'''
    lo = 0
    hi = array.shape[0] - 1
    while lo <= hi:
        mid = lo + (hi-lo)//2
        if ( key < array[mid]):
            hi = mid - 1
        elif (key > array[mid]):
            lo = mid + 1
        else:
            return mid
    return -1

def generate_array(size):
    array = np.random.randint(-1000000, 1000000, size)
    return array


def two_sum_brute_force(array):
    pass


def two_sum_quick(array):
    pass

def mesure_time(callback,array):
    start_time = time.time()
    callback(array)
    end_time = time.time()
    return end_time - start_time

    

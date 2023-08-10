'''This program implements the three sum algorithm and compares the running time of the brute force algorithm and the binary search algorithm.'''
import numpy as np
import time as t
import matplotlib.pyplot as plt
import os
import sys 

sys.path.insert(0,os.path.join(r'..\Sort'))
from Sort import MergeSort


def BinarySearch(array, key):
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

def ThreeSumBruteForce(inputArray):
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

    
def main():
    '''reads in the file and stores the values in an array'''
    array_sizes = [1000,2000,4000,8000]
    brute_force_times = []  # array to store the running time of the brute force algorithm
    quick_times = []  # array to store the running time of the quick algorithm
    file_names = ["1Kints.txt","2Kints.txt","4Kints.txt","8Kints.txt"]
    for file in file_names:
        data = np.loadtxt(os.path.join("D:/Data/",file))
        startTime = t.time()
        zeroSums = ThreeSumBruteForce(data)
        endTime = t.time()
        print(f"There are {zeroSums} in an array of {data.shape[0]} and it took {endTime-startTime} seconds to process Brute Force")
        brute_force_times.append(endTime-startTime)
        startTime = t.time()
        zeroSums = ThreeSumQuick(data)
        endTime = t.time()
        print(f"There are {zeroSums} in an array of {data.shape[0]} and it took {endTime-startTime} seconds to process Quick")
        quick_times.append(endTime-startTime)
    # plot the running time of the two algorithms on the same graph
    plt.plot(array_sizes, brute_force_times, label="Brute Force")
    plt.plot(array_sizes, quick_times, label="Quick")
    plt.xlabel("Array Size")
    plt.ylabel("Running Time")
    plt.title("Running Time of Brute Force vs Quick")
    plt.legend()
    plt.show()

        

if __name__ == "__main__":
    main()
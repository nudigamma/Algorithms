import numpy as np

def InsertionSort(array):
    '''input is an array of integers'''
    n = array.shape[0] # number of elements in the array

    for i in range(1,n):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key: #similar to bubble sort propagate the key to the left
            array[i] = array[j] #swap
            array[j] = key #swap 
            j = j - 1 # decrement j

           
        
    return array



def swapelement(i,j):
    '''swaps the ith and jth element of the array'''
    temp = i
    i = j
    j = temp
    return i,j

def BubbleSort(array,verbose=False):
    '''input is an array of integers'''
    n = array.shape[0] # number of elements in the array
    swapped = True
    count = 0 
    start = 0
    end = n-1
    while (swapped) :
        
        for i in np.arange(start,end):
            if array[i] > array[i+1]:
                array[i],array[i+1] = swapelement(array[i],array[i+1])
                swapped = True
                count += 1
        if swapped == False:
            break
        swapped = False
        end = end - 1
        for i in np.arange(end-1,start-1,-1):
            if array[i] > array[i+1]:
                array[i],array[i+1] = swapelement(array[i],array[i+1])
                swapped = True
                count += 1
        start = start + 1
        if verbose:
            print(f"Bubble Sort array = {array}")    
    return array,count

def MergeSort(array):
    '''This function implements the merge sort algorithm
    Input: numpy array of numbers
    Output: sorted numpy array of numbers
    '''

    c = np.zeros(array.shape[0])
    # base case
    if array.shape[0] == 1:
        return array
    else:
        # general case
        # we split the array in two and recursively call mergeSort
        right = MergeSort(array[0:array.shape[0]//2])
        left = MergeSort(array[array.shape[0]//2:])
        i = 0
        j = 0
        k = 0
        # while we are within the limits of the arrays
        # we merge the arrays
        while (i < right.shape[0]) and (j < left.shape[0]):
                if right[i] < left[j]:
                    c[k] = right[i]
                    i += 1
                else: 
                    c[k] = left[j] 
                    j += 1
                k += 1
        # we exited the above loop due to one of the arrays being exhausted
        # we now copy the remaining elements from the other array
        # if we are still within the limits of the right array we copy the remaining elements
        while i < right.shape[0]:
                c[k] = right[i]
                i += 1
                k += 1
        # if we are still within the limits of the left array we copy the remaining elements
        while j < left.shape[0]:
                c[k] = left[j]
                j += 1
                k += 1
        # we return the merged array
        return c
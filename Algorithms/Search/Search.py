import numpy as np
import platform
import sys
import os 


import sys
import os

# Get the current working directory
cwd = os.getcwd()

# Append the path to your module to the current working directory
module_path = os.path.join(cwd, 'Algorithms')
sys.path.append(module_path)

from Sort.Sort import MergeSort


def closestPairBruteForce1D(array):
    '''Find the closess Pair of points in a 1D array '''
    if len(array) == 0 or len(array) == 1:
        raise ValueError("input array needs to have more than one element")
    
    minDistance = np.inf
    min_p1, min_p2 = None, None
    minDistance = np.inf
    min_p1, min_p2 = ()
    # 1D array meaning it doesn't have y coordinate. 
    for x in range(len(array)):
        # we find the squared distance be
        for next_element in range(x,len(array)):
                d_2= (array[next_element] - array[x])**2 
                if  d_2 < minDistance:
                    minDistance = d_2
                    min_p1, min_p2 =  array[x], array[next_element]

    return min_p1,min_p2

def closestPoint1D(array):
    ''' docstring for closestPoint1D'''
    
    '''Find the closess Pair of points in a 1D array
    Args:
        array: a numpy array of integers
    Returns:
        a tuple of two integers
    Raises:
        ValueError: if the input array has less than two elements
    '''
    
    if len(array) == 0 or len(array) == 1:
        raise ValueError("input array needs to have more than one element")
    #sort the array
    array = MergeSort(array)
    minDistance = np.inf
    min_p1, min_p2 = None, None
    for x in range(len(array)-1):
        d_2= (array[x+1] - array[x])**2 
        if  d_2 < minDistance:
            minDistance = d_2
            min_p1, min_p2 =  array[x], array[x+1]
    return min_p1,min_p2

def closestDistance2DBruteForce(array):
    minDistance = np.inf
    if len(array) == 0 or len(array) == 1:
        raise ValueError("input array needs to have more than one element")

    min_p1, min_p2 = None, None
    minDistance = np.inf
    # 2D array meaning it doesn't have y coordinate. 
    for element in range(len(array)):
        # we find the squared distance be
        for next_element in range(element,len(array)):
                d_2= (array[element][0] - array[next_element][0])**2 + (array[element][1] - array[next_element][1])**2
                print(d_2)
                if  d_2 < minDistance and d_2 != 0:
                    minDistance = d_2
                    min_p1, min_p2 =  array[element], array[next_element]

    return min_p1,min_p2



<<<<<<< HEAD
def distance_squared(p1,p2):
    #find the 2D distance between two points
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2


def FindclosestPair(ArrayOfPoints):
    '''This function finds the closest pair using the divide and conquer algorithm'''
    if len(ArrayOfPoints) == 0 or len(ArrayOfPoints) == 1:
        raise ValueError("input array needs to have more than one element")
    if len(ArrayOfPoints) == 2:
        return ArrayOfPoints[0],ArrayOfPoints[1]
    
    #sort the array according to x coordinate
    ArrayOfPointsX = sorted(ArrayOfPoints, key=lambda x: x[0]) # assuming using mergesort   
    ArrayOfPointsY = sorted(ArrayOfPoints, key=lambda x: x[1]) # assuming using mergesort
    #divide the array into two halves
        #find the closest pair in the left half
    l1, l2 = closestPair(Lx,Ly)


def closestPair(SortedInX,SortedInY):
    '''Find the closess Pair of points in a 2D array '''
    # SortedInX will have at least three elements because of the findClosestPair condition on input 
    if len(SortedInX) <= 3: # find the smallest distance between the three points
        minDistance = np.inf
        min_p1, min_p2 = None, None
        for x in range(len(SortedInX)-1):
            for next_element in range(x,len(SortedInX)):
                d_2= (SortedInX[next_element][0] - SortedInX[x][0])**2 + (SortedInX[next_element][1] - SortedInX[x][1])**2
                if  d_2 < minDistance:
                    minDistance = d_2
                    min_p1, min_p2 =  SortedInX[x], SortedInX[next_element]
        return min_p1,min_p2
    #no need for else condition because if will return
    #divide the SortedInX into two halves
    Lx = SortedInX[0:len(SortedInX)//2]
    Rx = SortedInX[len(SortedInX)//2:]
    #divide the SortedInY into two halves
    Ly = SortedInY[0:len(SortedInY)//2]
    Ry = SortedInY[len(SortedInY)//2:]
    #find the closest pair in the left half
    l1, l2 = closestPair(Lx,Ly)
    #find the closest pair in the right half
    r1, r2 = closestPair(Rx,Ry)


        


=======
 
>>>>>>> c6498a8629e578d1eb2f390cce54c1239b984269
def SecondLargest(array):
    '''This function finds the second largest element in an array'''
    '''array is a numpy array of integers'''
    '''this function returns a numpy array of two elements, the first element is the largest element in the array, the second element is the second largest element in the array'''
    '''this function uses the divide and conquer algorithm'''
    if array.shape[0] == 1:
        return np.array([array[0],np.NINF])
    if array.shape[0] == 2:
        if array[0] > array[1]:
            return array
        else:
            temp = array[1]
            array[1] = array[0]
            array[0] = temp
            return array
    else:
        left  = SecondLargest(array[0:array.shape[0]//2])
        right  = SecondLargest(array[array.shape[0]//2:])
        

        if left[0] > right[0]:
            largest = left[0]
            if right [0] > left[1]:
                secondLargest = right[0]
            else:
                secondLargest = left[1]
        else :
            largest = right[0]
            if left[0] > right[1]:
                secondLargest = left[0]
            else:
                secondLargest = right[1]

        
        return np.array([largest,secondLargest])
    
def BinarySearch(array, key):
    '''perform binary search on a sorted array'''
    '''array is a numpy array of integers'''
    '''key is an integer'''
    '''this function returns the index of the key in the array'''
    '''if the key is not in the array, this function returns -1'''
    '''this function uses the iterative method'''
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

def main():

    test_array2_2D  = np.array([[9,2.5],[1,4],[5.5,-1],[4,3],[6,7],[5,11]])
    #2D closest pair
    print(closestDistance2DBruteForce(test_array2_2D))


if __name__ == "__main__":
    main()

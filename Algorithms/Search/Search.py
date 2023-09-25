import numpy as np
import platform
import sys
import os 

from Algorithms.Sort.Sort import MergeSort
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



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
                d_2= distance_squared(array[x],array[next_element])
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
                d_2= distance_squared(array[element],array[next_element])
                if  d_2 < minDistance and d_2 != 0:
                    minDistance = d_2
                    min_p1, min_p2 =  array[element], array[next_element]

    return min_p1,min_p2


def distance_squared(p1,p2):
    #find the 2D distance between two points
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2


import numpy as np
import platform
import sys
import os 

from Algorithms.Sort.Sort import MergeSort
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def closestPairBruteForce1D(array):
    pass

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
        for next_element in range(element+1,len(array)):
                d_2 = distance_squared(array[element],array[next_element])
                if  d_2 < minDistance :
                    minDistance = d_2
                    min_p1, min_p2 =  array[element], array[next_element]

    return min_p1,min_p2


def distance_squared(p1,p2):
    #find the 2D distance between two points
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2


def closestPair(SortedInX,SortedInY):
    '''Find the closess Pair of points in a 2D array '''
    # SortedInX will have at least three elements because of the findClosestPair condition on input 
    if len(SortedInX) == 0 :
        return (np.inf,np.inf),(np.inf,np.inf)
    if len(SortedInX) == 1:
        return SortedInX[0],(np.inf,np.inf)
    if len(SortedInX) == 2:
        return SortedInX[0],SortedInX[1]
    
    if len(SortedInX) == 3: # find the smallest distance between the three points
        return closestDistance2DBruteForce(SortedInX)
   
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
    d1 = distance_squared(l1,l2)
    d2 = distance_squared(r1,r2)
    delta = min(d1,d2)
    #find the closest pair that has one point in the left half and one point in the right half
    #s1,s2 = closestSplitPair(SortedInX,SortedInY,delta)
    #return the closest pair
    #d3 = distance_squared(s1,s2)
    return l1, l2, r1, r2, min(d1,d2)


def FindclosestPair(ArrayOfPoints):
    '''This function finds the closest pair using the divide and conquer algorithm'''
    if len(ArrayOfPoints) == 0 or len(ArrayOfPoints) == 1:
        raise ValueError("input array needs to have more than one element")
    if len(ArrayOfPoints) == 2:
        print(f"ArrayOfPoints = {ArrayOfPoints}")
        return ArrayOfPoints[0],ArrayOfPoints[1]
    
    #sort the array according to x coordinate
    
    PointsX = sorted(ArrayOfPoints, key=lambda x: x[0]) 
    PointsY = sorted(PointsX, key=lambda x :x[1])
    
    #divide the array into two halves
    #find the closest pair in the left half
    
    return  (closestPair(PointsX,PointsY))

def closestPair(SortedInX,SortedInY):
    '''Find the closess Pair of points in a 2D array '''
    # SortedInX will have at least three elements because of the findClosestPair condition on input 
    
    
    
    if len(SortedInX) <= 3: # find the smallest distance between the three points
        return closestDistance2DBruteForce(SortedInX)
    
   
    #no need for else condition because if will return
    #divide the SortedInX into two halves
    Lx = SortedInX[0:len(SortedInX)//2]
    Rx = SortedInX[len(SortedInX)//2:]
    #Ly is lx sorted according to y coordinate
    #Ly = sorted(Lx,key=lambda x:x[1])
    Ly = SortedInY[0:len(SortedInY)//2]
    #Ry is rx sorted according to y coordinate
    #Ry = sorted(Rx,key=lambda x:x[1])
    Ry = SortedInY[len(SortedInY)//2:]
    #find the closest pair in the left half
    l1, l2 = closestPair(Lx,Ly)
    #find the closest pair in the right half
    r1, r2 = closestPair(Rx,Ry)
    d1 = distance_squared(l1,l2)
    d2 = distance_squared(r1,r2)
    delta = min(d1,d2)
    print(f"delta = {delta}")
    #find the closest pair that has one point in the left half and one point in the right half
    s1,s2 = closestSplitPair(SortedInX,SortedInY,delta)
    #return the closest pair
    d3 = distance_squared(s1,s2)
    if d1 < d2:
        if d1 < d3:
            return l1, l2
        else:
            return s1,s2
    else:
        if d2 < d3:
            return r1, r2
        else:
            return s1,s2



def closestSplitPair(SortedInX, SortedInY, delta):
    # Find the middle point, it should be the last point in the left half
    middlePoint = SortedInX[len(SortedInX) // 2-1][0]
    print(f"middlePoint = {middlePoint}")
    
    # Find the points that belong to Sy which are between middlePoint - delta and middlePoint + delta
    Sy = [point for point in SortedInY if middlePoint - delta <= point[0] <= middlePoint + delta]
    print(f"Sy = {Sy}")
    
    # Check if Sy has less than two points
    if len(Sy) < 2:
        return (-np.inf, -np.inf), (np.inf, np.inf)  # Return a default pair; this will be ignored due to the larger distance.
    
    # Initialize the ClosestPair to the first two points of Sy
    ClosestPair = Sy[0], Sy[1]
    ClosestDistance = delta #distance_squared(Sy[0], Sy[1])
    
    for i in range(len(Sy) - 1):
        for j in range(i + 1, min(i + 8, len(Sy))):
            d = distance_squared(Sy[i], Sy[j])
            
            # Ensure we're not comparing the same point against itself
            if d == 0:
                continue
                
            if d < ClosestDistance:
                ClosestDistance = d
                ClosestPair = Sy[i], Sy[j]
    
    return ClosestPair[0], ClosestPair[1]

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

def BinarySearchRecursive(array, key):

    if array.shape[0] == 0:
        return -1
    if array.shape[0] == 1:
        if array[0] == key:
            return 0
        else:
            return -1
    
    mid = array.shape[0]//2
    if array[mid] == key:
        return mid
    elif array[mid] > key:
        return BinarySearchRecursive(array[0:mid],key)
    else:
        return BinarySearchRecursive(array[mid+1:],key)
    
    
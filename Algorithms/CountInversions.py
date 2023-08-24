'''this program implement count inversions algorithm using brute force and divide and conquer method'''

# Brute force method

def bruteForeCountInversion(array):
    '''this function counts the number of inversions in an array using brute force method'''
    '''input : array of integers'''
    '''output : number of inversions in the array'''
    '''time complexity : O(n^2)'''
    inversionCount = 0
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i] > array[j]:
                inversionCount += 1
    return inversionCount

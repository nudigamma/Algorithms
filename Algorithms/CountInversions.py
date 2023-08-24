'''this program implement count inversions algorithm using brute force and divide and conquer method'''

# Brute force method

def bruteForeCountInversion(array):
    inversionCount = 0
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i] > array[j]:
                inversionCount += 1
    return inversionCount

'''this is the implementation of the Rselect algorithm'''
import random
def partition(array : list,left : int , right : int ) -> int :
    ''' this function partitions the array around a pivot value'''
    if left >= right :
        return -1
    pivot_value = array[left]
    lesser_index = left + 1
    for index,value in enumerate(array[left+1:right+1],left+1):
        if value < pivot_value:
            array[lesser_index], array[index] = array[index], array[lesser_index]
            lesser_index += 1
    array[left], array[lesser_index-1] = array[lesser_index-1], array[left]
    return lesser_index-1
    
def Rselect(array, left, right, ith):
    if left >= right:
        return array[left]

    p_pivot_index = random.randint(left, right)
    array[left], array[p_pivot_index] = array[p_pivot_index], array[left]

    pivot_index = partition(array, left, right)

    if pivot_index == ith:
        return array[pivot_index]
    elif pivot_index > ith:
        return Rselect(array, left, pivot_index - 1, ith)  # Corrected pivot_index
    else:
        return Rselect(array, pivot_index + 1, right, ith - pivot_index -1)

if __name__ == '__main__':
    array = [3,2,1,5,4,6,7,8,9,10]
    print(Rselect(array,0,len(array)-1,3))
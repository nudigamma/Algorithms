'''this is the implementation of the Rselect algorithm'''

def partition(array : list,left : int , right : int ) -> int :
    ''' this function partitions the array around a pivot value'''
    pivot_value = array[left]
    lesser_index = left + 1
    for index,value in enumerate(array[lesser_index:right]):
        if value < pivot_value:
            array[lesser_index], array[index] = array[index], array[lesser_index]
            lesser_index += 1
    array[left], array[lesser_index-1] = array[lesser_index-1], array[left]
    return lesser_index-1
    
def Rselect(array : list, left : int, right : int, ith : int) -> int :
    '''this function returns the ith order statistic of the array'''
    if left >= right:
        return array[0]
    # we choose a random pivot
    pivot_index = np.random.randint(left,right)
    array[left], array[pivot_index] = array[pivot_index], array[left]
    position = partition(array,left,right)
    if position == ith:
        return position
    elif ith < position:
        return Rselect(array,left,position,ith)
    else:
        return Rselect(array,pivot_index+1,right,ith-position-1)



# test the algorithm 

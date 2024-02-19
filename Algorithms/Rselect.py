import random

def partition(array, left, right):
    pivot_value = array[left]
    i = left + 1
    for j in range(left + 1, right + 1):
        if array[j] < pivot_value:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[left], array[i - 1] = array[i - 1], array[left]
    return i - 1

def Rselect(array, left, right, ith):
    if left == right:
        return array[left]

    pivot_index = random.randint(left, right)
    array[left], array[pivot_index] = array[pivot_index], array[left]
    new_pivot_index = partition(array, left, right)

    if new_pivot_index == ith:
        return array[new_pivot_index]
    elif new_pivot_index > ith:
        return Rselect(array, left, new_pivot_index - 1, ith)
    else:
        return Rselect(array, new_pivot_index + 1, right, ith)

if __name__ == '__main__':
    accumulator = 0
    test_iteration_number = 100000
    for _ in range(test_iteration_number):
        array = [3, 2, 1, 5, 4, 6, 7, 8, 9, 10]
        accumulator += Rselect(array, 0, len(array) - 1, 3)
    print(accumulator / test_iteration_number)

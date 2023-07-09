import matplotlib.pyplot as plt
import sys
from InsertionSort import insertionSort
from BubbleSort import bubbleSort

sys.path.insert(0, r'D:\\source\\Algorithms-Iluminated\\part1_ basics')
import Utils.RandomDataGenerator as rnd

def main():
    array = rnd.generateRandomArray(10,100,-10000,10000)
    array_copy = array.copy()
    print(f"array = {array}")
    sorted_array,insertion_count = insertionSort(array,verbose=True)
    sorted_array,bubble_count = bubbleSort(array_copy,verbose=True)
    print(f"Array Size = {array.shape[0]} insertion_count = {insertion_count}")
    print(f"Array Size = {array.shape[0]} bubble_count = {bubble_count}")

if __name__ == '__main__':
    main()

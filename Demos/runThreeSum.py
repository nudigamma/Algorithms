import time as t
import matplotlib.pyplot as plt
import os
import sys 
import numpy as np
import platform as pl


thisscripterdir = os.path.dirname(os.path.abspath(__file__))
dirs = thisscripterdir.split(os.sep)
dirs.pop()
dirs.append("Algorithms")
dirs.append("Nsum")

thisscripterdir = os.sep.join(dirs)
sys.path.append(thisscripterdir)


from ThreeSum import ThreeSumBruteForce, ThreeSumQuick

def main():
    '''reads in the file and stores the values in an array'''
    array_sizes = [1000,2000,4000,8000]
    brute_force_times = []  # array to store the running time of the brute force algorithm
    quick_times = []  # array to store the running cd time of the quick algorithm
    file_names = ["1Kints.txt","2Kints.txt","4Kints.txt","8Kints.txt"]
    for file in file_names:
        data = np.loadtxt(os.path.join('..','..', '..', 'Data', file))
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
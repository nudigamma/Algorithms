'''This program implements the three sum algorithm and compares the running time of the brute force algorithm and the binary search algorithm.'''
import numpy as np
import time as t
import matplotlib.pyplot as plt
import os



def ThreeSumBruteForce(inputArray):
    count = 0
    for i in np.arange(inputArray.size):
        
        for j  in np.arange(i+1,inputArray.size):
             
            for z in np.arange(j+1,inputArray.size):
                
                if inputArray[i] + inputArray[j] + inputArray[z] == 0:
                    count +=1
                    
     

    return count

def ThreeSumVectorized(inputArray):
    '''this function implements the three sum algorithm using the vectorized approach'''
    count = 0
    
def main():
    '''reads in the file and stores the values in an array'''
    
    file_names = ["1Kints.txt","2Kints.txt","4Kints.txt","8Kints.txt"]
    for file in file_names:
        data = np.loadtxt(os.path.join("D:/Data/",file))
        startTime = t.time()
        zeroSums = ThreeSumBruteForce(data)
        endTime = t.time()
        print(f"There are {zeroSums} in an array of {data.shape[0]} and it took {endTime-startTime} seconds to process")

if __name__ == "__main__":
    main()
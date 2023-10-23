import time as t
import matplotlib.pyplot as plt
import os
import sys 
import numpy as np
import unittest


thisscripterdir = os.path.dirname(os.path.abspath(__file__))
dirs = thisscripterdir.split(os.sep)
dirs.pop()
dirs.append("Algorithms")

thisscripterdir = os.sep.join(dirs)


sys.path.append(thisscripterdir)



dirs.pop() 
dirs.append("Data")
datadirs = os.sep.join(dirs)


from Search import ThreeSumBruteForce, ThreeSumQuick

# need to write a unit test 


class Test3Sum (unittest.TestCase):
    '''reads in the file and stores the values in an array'''
    def test_correctness(self):
            print("HERE")
            file_names = ["1Kints.txt","2Kints.txt","4Kints.txt"]
            expected_results = [70,528,4039] # values from Sedgwick Algorithm book
            for index, file in enumerate(file_names):
                file_path = os.path.join(datadirs, file)
                data = np.loadtxt(file_path)
                zeroSums, triplets= ThreeSumQuick(data)
                assert(zeroSums == expected_results[index])
                print(f"Test Passed for {file[:2]} Integers")
        

if __name__ == "__main__":
    unittest.main()


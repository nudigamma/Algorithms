import time as t
import matplotlib.pyplot as plt
import os
import sys 
import numpy as np
import unittest


thisscripterdir = os.path.dirname(os.path.abspath(__file__))
dirs = thisscripterdir.split(os.sep)

dirs.pop()
data_dir = dirs.copy()
data_dir.append("Data")
dirs.append("Algorithms")
dirs.append("Search")

thisscripterdir = os.sep.join(dirs)
datadir = os.sep.join(data_dir)
sys.path.append(thisscripterdir)


from Search import ThreeSumBruteForce, ThreeSumQuick

# need to write a unit test 

class Test3Sum (unittest.TestCase):
    '''reads in the file and stores the values in an array'''
    def TestCorrectness(self):
            file_names = ["1Kints.txt","2Kints.txt","4Kints.txt"]#"8Kints.txt"]
            expected_results = [70,528,4039] # values from Sedgwick Algorithm book
            for index, file in enumerate(file_names):
                data = np.loadtxt(os.path.join(datadir, file))
                zeroSums = ThreeSumQuick(data)
                assert(zeroSums == expected_results[index])
        

if __name__ == "__main__":
    unittest.main()

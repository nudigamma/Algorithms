'''This program implements the three sum algorithm and compares the running time of the brute force algorithm and the binary search algorithm.'''
import numpy as np
import os 
import sys
import platform as pl

    
thisscripterdir = os.path.dirname(os.path.abspath(__file__))
dirs = thisscripterdir.split(os.sep)
dirs.pop()
dirs.append("Sort")
thisscripterdir = os.sep.join(dirs)
sys.path.append(thisscripterdir)
dirs.pop()
dirs.append("Search")
thisscripterdir = os.sep.join(dirs)
sys.path.append(thisscripterdir)




from Sort import MergeSort
from Search import BinarySearch


    

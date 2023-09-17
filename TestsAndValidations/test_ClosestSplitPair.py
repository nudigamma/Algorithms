import numpy as np
import unittest
import sys
import socket 
import os
# get os type
import os 
import sys 
import platform
import random

    

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
print(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Algorithms.Search.Search import closestDistance2DBruteForce, FindclosestPair, distance_squared, closestSplitPair

class TestClosestPair(unittest.TestCase):
    


    
    def test_closestPair(self):
        # test case that assumes that the closest pair is in the left half
        # of the array
        array = [(1,2),(2,1),(2,5),(5,2),(6,4),(9,.5),(9,1)]
        print("testing closest pair when the closest pair is in the left half of the array")
        p1,p2,= FindclosestPair(array)
        assert p1 == (9,.5)
        assert p2 == (9,1)
        print("Test Passed")
        # test case that assumes that the closest pair is in the right half
        array = [(1.75,2),(2,1.75),(2,5),(5,2),(6,4),(9,.5),(9,1)]
        print("testing closest pair when the closest pair is in the right half of the array")
        p1,p2 = FindclosestPair(array)
        assert p1 == (1.75,2)
        assert p2 == (2,1.75)
        print("Test Passed")
    def test_closestSplitPair(self):
        '''tests the closest split pair part of the algorithm'''
        print("testing closest pair when the closest pair is split between the left and right halves of the array")
        array = [(1,8),(2,5),(6,3),(4,7)]
        p1,p2= FindclosestPair(array)
        assert p1 == (2,5)
        assert p2 ==  (4,7)

    def test_closestSplitPairBigArray(self):

        # Seed for reproducibility
        random.seed(42)

        # Generate dense cluster on the left
        left_cluster = [(random.uniform(0, 1), random.uniform(0, 1)) for _ in range(100)]

        # Generate dense cluster on the right
        right_cluster = [(random.uniform(4, 5), random.uniform(4, 5)) for _ in range(100)]

        # Generate points in the middle
        middle_points = [(random.uniform(2, 3), random.uniform(2, 3)) for _ in range(10)]

        # Combine all points
        points = left_cluster + middle_points + right_cluster

        # Shuffle to randomize the order
        random.shuffle(points)

        # Find the closest pair
        p1, p2 = FindclosestPair(points)
        p1brute,p2brute = closestDistance2DBruteForce(points)
        assert p1 == p1brute
        assert p2 == p2brute

def main():
    unittest.main()

if __name__ == '__main__':
    main()
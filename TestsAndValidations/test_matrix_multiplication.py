
import numpy as np
import unittest
import sys
import socket 
import os
# get os type
import os 
import sys 
import platform
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Algorithms.MatrixMultiplication.MatMul import VecDot, MatMul, RecMatMult, strassenRecMat


class TestMatrixMultiplication(unittest.TestCase):

# now test the matmul function on square matrices 4x4 
    for step in np.arange(10,20):
        n = 2**step
        X = np.float32(np.random.randint(0,10,(n,n)))
        Y = np.float32(np.random.randint(0,10,(n,n)))
# compare element wise matrix members and assert that they are equal
        startTime = time.time()
        XY = np.matmul(X,Y)
        endTime = time.time()
        print(f"MatMul(X,Y) took {endTime - startTime} seconds for n = {n}")
        assert np.allclose(np.matmul(X,Y),XY)
    
        startTime = time.time()
        XY = RecMatMult(X,Y)
        endTime = time.time()
        print(f"RecMatMult(X,Y) took {endTime - startTime} seconds for n = {n}")
        assert np.allclose(np.matmul(X,Y),XY)
    
        startTime = time.time()
        XY = strassenRecMat(X,Y)
        endTime = time.time()
        print(f"strassenRecMat(X,Y) took {endTime - startTime} seconds for n = {n}")
        assert np.allclose(np.matmul(X,Y),XY)


if __name__ == '__main__':
    unittest.main()

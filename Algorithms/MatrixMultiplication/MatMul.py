'''this file implements the matrix multiplication algorithm'''
'''first we implement the dot product of two vectors'''
import numpy as np

def VecDot(a,b):
    dot = 0
    if a.shape[0] != b.shape[0]:
        return None
    for i in np.arange(a.shape[0]):
        dot += a[i] * b[i]
    return dot

def MatMul(A,B):
    if A.shape[1] != B.shape[0]:
        print("Make sure that M of columns of A is equal to N columns of B\n")
        return None
    C = np.zeros((A.shape[0],B.shape[1]))
    for row in np.arange(A.shape[0]):
        for column in np.arange(B.shape[1]):
            C[row,column] = VecDot(A[row,:],B[:,column])
    return C


# now test the VecDot function
a = np.array([1,2,3])
b = np.array([4,5,6])
#print(np.dot(a,b))
#print(VecDot(a,b)) 
assert VecDot(a,b) == np.dot(a,b)

# now test the MatMul function on square matrices 2x2
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
print(np.matmul(A,B))
print(MatMul(A,B))
# now test the MatMul function on non square matrices 2x3 and 3x2
A = np.array([[1,2,3],[4,5,6]])
B = np.array([[7,8],[9,10],[11,12]])
print(np.matmul(A,B))
print(MatMul(A,B))
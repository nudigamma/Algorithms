''' this program implements the pseudocode for recursive integer multiplication @page 9 of the book Algorithm Illuminated Part 1: The Basics'''

''' Pseudocode 
recursiveIntegerMultiplication
Input: Two n-digit positive integers number1 and number2
Output: The product number1*number2
Assumption : n is a power of 2, and x and y have the same number of digits, n
# Base case
if n = 1 then
    return number1*number2
# Recursive case
else
    a,b = first and second halves of number1, where x = 10**(n/2)*a + b
    c,d = first and second halves of number2, where y = 10**(n/2)*c + d
    compute ac = a*c recursively
    compute bd = b*d recursively
    conpute ad = a*d recursively
    compute bc = b*c recursively
    return 10**n*ac + 10**(n/2)*(ad + bc) + bd


'''

import numpy as np
import unittest
import time 
        
def recursiveIntegerMultiplication(number1, number2,n1,n2):
    '''Assumption: number1 and number2 are of the same size and there size is a power of 2'''
    # Base case
   
    if n1== 1:
        return number1 * number2
    # Recursive case
    else:
        a,b = number1 // 10**(n1//2), number1 % 10**(n1//2)
        c,d = number2 // 10**(n2//2), number2 % 10**(n2//2)
        n3 = n1//2
        n4 = n2//2  
        ac = recursiveIntegerMultiplication(a,c,n3,n4)
        bd = recursiveIntegerMultiplication(b,d,n3,n4)
        ad = recursiveIntegerMultiplication(a,d,n3,n4)
        bc = recursiveIntegerMultiplication(b,c,n3,n4)
        return 10**(n1)*ac + 10**(n3)*(ad+bc) + bd

def karatsubaMultiplication(number1, number2,n1,n2):
    '''Assumption: number1 and number2 are of the same size and there size is a power of 2'''
    # Base case
    if n1== 1:
        return number1 * number2
    # Recursive case
    else:
        a,b = number1 // 10**(n1//2), number1 % 10**(n1//2)
        c,d = number2 // 10**(n2//2), number2 % 10**(n2//2)
        p = a+b
        q = c+d
        n3 = n1//2
        n4 = n2//2  
        ac = recursiveIntegerMultiplication(a,c,n3,n4)
        bd = recursiveIntegerMultiplication(b,d,n3,n4)
        pq = recursiveIntegerMultiplication(p,q,n3,n4)
        adbc = pq - ac - bd
        return 10**(n1)*ac + 10**(n3)*(adbc) + bd




class TestRecursiveIntegerMultiplication(unittest.TestCase):

    def test_recursive_multiplication(self):
        number_of_tests = 3000
        print(f"Generating {number_of_tests} tests \n")
        start = time.time()
        for i in range(number_of_tests):
            for n in range(0, 4):

                # Generate two random numbers of size n**2
                
                low = 10**(2**n)
                high = 10**(2**n+1)-1
                num1 = np.random.randint(low, high)
                num2 = np.random.randint(low, high)
                
                n1 = n2 = 2**n
                # Check if the product computed by the recursive algorithm is the same as the built-in multiplication result
        
                assert np.abs(recursiveIntegerMultiplication(num1, num2, n1, n2) - (num1 * num2)) == 0, f"Test failed for num1={num1}, num2={num2}, n={n}"
        end = time.time()
        print(f"Time taken for {number_of_tests} tests is {end-start} seconds")

    def test_karatsuba_multiplication(self):
        number_of_tests = 3000
        print(f"Generating {number_of_tests} tests \n")
        start = time.time()
        for i in range(number_of_tests):
            for n in range(0, 4):

                # Generate two random numbers of size n**2
                
                low = 10**(2**n)
                high = 10**(2**n+1)-1
                num1 = np.random.randint(low, high)
                num2 = np.random.randint(low, high)
                
                n1 = n2 = 2**n
                # Check if the product computed by the recursive algorithm is the same as the built-in multiplication result
        
                assert np.abs(karatsubaMultiplication(num1, num2, n1, n2) - (num1 * num2)) == 0, f"Test failed for num1={num1}, num2={num2}, n={n}"
        end = time.time()
        print(f"Time taken for {number_of_tests} tests is {end-start} seconds")
        
if __name__ == '__main__':
    unittest.main()
    

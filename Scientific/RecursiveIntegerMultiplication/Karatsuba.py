''' this program implements the pseudocode for recursive integer multiplication @page 9 of the book Algorithm Illuminated Part 1: The Basics'''
''' Check Karatsuba.pdf for the discussion of the Algorithm''' 

import numpy as np
import unittest
import time 
        


def karatsubaMultiplication(number1, number2,n1,n2):
    '''Assumption: number1 and number2 are of the same size and there size is a power of 2'''
    # Base case
    if n1== 1:
        return number1 * number2
    # Recursive case
    else:
        a = number1 // 10**(n1//2)
        b = number1 % 10**(n1//2) 
        c = number2 // 10**(n2//2) 
        d = number2 % 10**(n2//2) 
        p = a+b
        q = c+d
        n3 = n1//2
        n4 = n2//2  
        ac = karatsubaMultiplication(a,c,n3,n4)
        bd = karatsubaMultiplication(b,d,n3,n4)
        pq = karatsubaMultiplication(p,q,n3,n4)
        adbc = pq - ac - bd
        return 10**(n1)*ac + 10**(n3)*(adbc) + bd




class TestKaratsubaMultiplication(unittest.TestCase):

    def test_karatsuba_multiplication_random(self):
        number_of_tests = 3000
        print(f"Generating {number_of_tests} tests \n")
        start = time.time()
        for i in range(number_of_tests):
                n = 8
                # Generate two random numbers of size n**2
                num1 = np.random.randint(10**(n-1), 10**n -1)
                num2 = np.random.randint(10**(n-1), 10**(n) -1)
                n1 = n2 = 8
                # Check if the product computed by the recursive algorithm is the same as the built-in multiplication result
        
                assert np.abs(karatsubaMultiplication(num1, num2, n1, n2) - (num1 * num2)) == 0, f"Test failed for num1={num1}, num2={num2}, n={n}"
        end = time.time()
        print(f"Time taken for {number_of_tests} tests is {end-start} seconds")

    def test_karatsuba_multiplication_chap1_(self):
        n1 = 3141592653589793238462643383279502884197169399375105820974944512   
        n2 = 2718281828459045235360287471352662497757247093699959574966967612
        n = len(str(n1))
        product_recursive = karatsubaMultiplication(n1, n2, n, n)
        product_builtin = n1*n2
        #error in the recursive algorithm
        assert  np.abs(product_recursive - product_builtin) == 0, f"Test failed for num1={n1}, num2={n2}, n={n}"
        
if __name__ == '__main__':
   unittest.main()
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

karatsubaMultiplication very similar to above but with 3 recursive calls instead of 4
Input: Two n-digit positive integers number1 and number2
Output: The product number1*number2
Assumption : n is a power of 2, and x and y have the same number of digits, n
# Base case
if n = 1 then
    return number1*number2
# Recursive case
else
    a,b = first and second halves of number1, where x = 10**(n/2)*a + b, then a = x//10**(n/2), b = x % 10**(n/2)
    c,d = first and second halves of number2, where y = 10**(n/2)*c + d
    p = a+b
    q = c+d
    
    compute ac = a*c recursively
    compute bd = b*d recursively
    compute pq = p*q recursively
    compute adbc = pq - ac - bd
    return 10**n*ac + 10**(n/2)*(adbc) + bd
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
        a = number1 // 10**(n1//2)
        b = number1 % 10**(n1//2)
        c = number2 // 10**(n2//2) 
        d = number2 % 10**(n2//2) 
        n3 = n1//2
        n4 = n2//2  
        ac = recursiveIntegerMultiplication(a,c,n3,n4)
        bd = recursiveIntegerMultiplication(b,d,n3,n4)
        ad = recursiveIntegerMultiplication(a,d,n3,n4)
        bc = recursiveIntegerMultiplication(b,c,n3,n4)
        return 10**(n1)*ac + 10**(n3)*(ad+bc) + bd






class TestRecursiveIntegerMultiplication(unittest.TestCase):

    def test_recursive_multiplication_random(self):
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
        
                assert np.abs(recursiveIntegerMultiplication(num1, num2, n1, n2) - (num1 * num2)) == 0, f"Test failed for num1={num1}, num2={num2}, n={n}"
        end = time.time()
        print(f"Time taken for {number_of_tests} tests is {end-start} seconds")

    def recursive_multiplication_chap1_ex_1_8(self):
        n1 = 3141592653589793238462643383279502884197169399375105820974944512    
        n2 = 2718281828459045235360287471352662497757247093699959574966967612
        n = len(str(n1))
        product_recursive = recursiveIntegerMultiplication(n1, n2, n, n)
        product_builtin = n1*n2
        #error in the recursive algorithm
        assert  np.abs(product_recursive - product_builtin) == 0, f"Test failed for num1={n1}, num2={n2}, n={n}"


        
if __name__ == '__main__':
    unittest.main()
    

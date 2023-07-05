''' this program implements the pseudocode for recursive integer multiplication @page 9 of the book Algorithm Illuminated Part 1: The Basics'''

import numpy as np
import unittest
        
def recursiveIntegerMultiplication(number1, number2,n1,n2):
    
    '''Assumption: number1 and number2 are of the same size and there size is a power of 2'''
    if n1== 1:
        return number1 * number2
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


def get_number_of_digits(number):
    return len(str(abs(number)))

class TestRecursiveIntegerMultiplication(unittest.TestCase):

    def test_recursive_multiplication(self):
        number_of_tests = 3000
        print(f"Generating {number_of_tests} tests")
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
        
if __name__ == '__main__':
    unittest.main()
    

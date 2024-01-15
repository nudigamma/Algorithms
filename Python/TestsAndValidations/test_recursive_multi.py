class TestKaratsubaMultiplication(unittest.TestCase):
    def test_karatsuba_multiplication(self):
        starttime = time.time()
        for _ in range(30000):
            # Generate two random numbers with the same number of digits (between 1 and 10)
            num_digits = random.randint(1, 10)
            number1 = random.randint(10**(num_digits-1), 10**num_digits - 1)
            number2 = random.randint(10**(num_digits-1), 10**num_digits - 1)

            # Calculate padding and pad the numbers
            padding_1 = getPaddingsize(number1)
            padding_2 = getPaddingsize(number2)
            padded_number1 = padNumber(number1, padding_1)
            padded_number2 = padNumber(number2, padding_2)

            # Perform Karatsuba multiplication and unpad the result
            result = karatsubaMultiplication(int(padded_number1), int(padded_number2), 
                                                  getNumDigits(padded_number1), getNumDigits(padded_number2))
            result = unpadNumber(result, padding_1 + padding_2)
            # Assert that the result is correct
            self.assertEqual(result, number1 * number2)
        endtime = time.time()
        print("Time taken for Karatsuba multiplication is ", endtime - starttime)
    
    def test_recursive_multiplication(self):
            starttime = time.time()
            for _ in range(30000):
            # Generate two random numbers with the same number of digits (between 1 and 10)
                num_digits = random.randint(1, 10)
                number1 = random.randint(10**(num_digits-1), 10**num_digits - 1)
                number2 = random.randint(10**(num_digits-1), 10**num_digits - 1)

            # Calculate padding and pad the numbers
                padding_1 = getPaddingsize(number1)
                padding_2 = getPaddingsize(number2)
                padded_number1 = padNumber(number1, padding_1)
                padded_number2 = padNumber(number2, padding_2)

            # Perform Karatsuba multiplication and unpad the result
                result = recursiveIntegerMultiplication(int(padded_number1), int(padded_number2), 
                                                  getNumDigits(padded_number1), getNumDigits(padded_number2))
                result = unpadNumber(result, padding_1 + padding_2)
            # Assert that the result is correct
                self.assertEqual(result, number1 * number2)
            endtime = time.time()
            print("Time taken for Recursive multiplication is ", endtime - starttime)
    def test_karatsuba_assignmnet(self):
        number1 =  3141592653589793238462643383279502884197169399375105820974944592
        number2 =  2718281828459045235360287471352662497757247093699959574966967627
        padding_1 = getPaddingsize(number1)
        padding_2 = getPaddingsize(number2)
        padded_number1 = padNumber(number1, padding_1)
        padded_number2 = padNumber(number2, padding_2)

        # Perform Karatsuba multiplication and unpad the result
        result = karatsubaMultiplication(int(padded_number1), int(padded_number2), 
                                                  getNumDigits(padded_number1), getNumDigits(padded_number2))
        result = unpadNumber(result, padding_1 + padding_2)
        print(result)
            # Assert that the result is correct
        self.assertEqual(result, number1 * number2)

# Run the unit test
unittest.main(argv=[''], exit=False)
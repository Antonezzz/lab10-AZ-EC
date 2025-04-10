#https://github.com/Antonezzz/lab10-AZ-EC
#Partner 1: Anthony Zheng
#Partner 2: Edgar Canaan

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ####### Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2, 5))
        self.assertAlmostEqual(mul(1.5, 2.25))
        self.assertEqual(mul(-1,5))

    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(div(10,5))
        self.assertAlmostEqual(div(0,0))
        self.assertAlmostEqual(div(-1,2))

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ####### Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0,5)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(1,5))
        self.assertAlmostEqual(hypotenuse(-11,5))
        self.assertAlmostEqual(hypotenuse(1,0.5))


    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(a)
        self.assertEqual(square_root(1,2))
        self.assertEqual(square_root(5,-2))
        self.assertEqual(0.5,5)

# Do not touch this
if __name__ == "__main__":
    unittest.main()
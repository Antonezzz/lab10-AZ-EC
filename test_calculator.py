#https://github.com/Antonezzz/lab10-AZ-EC
#Partner 1: Anthony Zheng
#Partner 2: Edgar Canaan

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2,2),4)
        self.assertAlmostEqual(add(-2,3.2), 1.2)
        self.assertEqual(add(0,1000), 1000)



    def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################
        self.assertEqual(subtract(5,2),3)
        self.assertAlmostEqual(subtract(3.1, 2.6), 0.5)
        self.assertEqual(subtract(-4, -3), -7)

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
    def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

        with self.assertRaises(ZeroDivisionError):
            div(0,5)




    def test_logarithm(self): # 3 assertions
    #     fill in code
        self.assertEqual(logarithm(10, 100), 2)
        self.assertAlmostEqual(logarithm(100, 10), 0.5)
        self.assertAlmostEqual(logarithm(8,2), 3)

    def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
        with self.assertRaises(ValueError):
            logarithm(0,0)


    
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
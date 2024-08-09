import unittest
from challenge2 import FirstFactorial

class TestFirstFactorial(unittest.TestCase):
    
    def test_factorial_of_1(self):
        self.assertEqual(FirstFactorial(1), 1)
    
    def test_factorial_of_2(self):
        self.assertEqual(FirstFactorial(2), 2)
    
    def test_factorial_of_5(self):
        self.assertEqual(FirstFactorial(5), 120)
    
    def test_factorial_of_10(self):
        self.assertEqual(FirstFactorial(10), 3628800)
    
    def test_factorial_of_18(self):
        self.assertEqual(FirstFactorial(18), 6402373705728000)
    
    def test_factorial_of_0(self):
        with self.assertRaises(ValueError):
            FirstFactorial(0)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            FirstFactorial(-5)
    
if __name__ == '__main__':
    unittest.main()
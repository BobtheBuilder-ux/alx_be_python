import unittest

def calculate_square(number):
    """
    Calculate the square of a number.
    Bug: Adds the number to itself instead of multiplying
    """
    # Intentionally buggy implementation
    return number + number  # Bug: This adds instead of multiplying

class TestCalculator(unittest.TestCase):
    def test_positive_number(self):
        """Test squaring a positive number"""
        self.assertEqual(calculate_square(4), 16)  # Should fail: 4+4 != 4*4
    
    def test_zero(self):
        """Test squaring zero"""
        self.assertEqual(calculate_square(0), 0)
    
    def test_negative_number(self):
        """Test squaring a negative number"""
        self.assertEqual(calculate_square(-3), 9)  # Should fail: -3+-3 != (-3)*(-3)
    
    def test_large_number(self):
        """Test squaring a large number"""
        self.assertEqual(calculate_square(100), 10000)  # Should fail: 100+100 != 100*100
    
    def test_float_number(self):
        """Test squaring a float number"""
        self.assertAlmostEqual(calculate_square(2.5), 6.25)  # Should fail: 2.5+2.5 != 2.5*2.5

if __name__ == '__main__':
    unittest.main()
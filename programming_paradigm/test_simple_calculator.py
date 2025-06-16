import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method with various scenarios."""
        # Test positive numbers
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(0, 5), 5)
        
        # Test negative numbers
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)
        
        # Test floating point numbers
        self.assertAlmostEqual(self.calc.add(2.5, 3.5), 6.0)

    def test_subtraction(self):
        """Test the subtraction method with various scenarios."""
        # Test positive numbers
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(5, 5), 0)
        
        # Test negative numbers
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(1, -1), 2)
        
        # Test floating point numbers
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.5), 3.0)

    def test_multiplication(self):
        """Test the multiplication method with various scenarios."""
        # Test positive numbers
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        
        # Test negative numbers
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        
        # Test floating point numbers
        self.assertAlmostEqual(self.calc.multiply(2.5, 2.0), 5.0)

    def test_division(self):
        """Test the division method with various scenarios."""
        # Test positive numbers
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertEqual(self.calc.divide(0, 5), 0)
        
        # Test negative numbers
        self.assertEqual(self.calc.divide(-6, 2), -3)
        self.assertEqual(self.calc.divide(-6, -2), 3)
        
        # Test floating point numbers
        self.assertAlmostEqual(self.calc.divide(5.0, 2.0), 2.5)
        
        # Test division by zero
        self.assertIsNone(self.calc.divide(5, 0))

if __name__ == '__main__':
    unittest.main()
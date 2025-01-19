import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-5, -10), -15)

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(-5, -5), 0)
        self.assertEqual(self.calc.subtract(0, 10), -10)
        self.assertEqual(self.calc.subtract(7, 0), 7)

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 10), 0)
        self.assertEqual(self.calc.multiply(-3, -3), 9)

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-9, 3), -3)
        self.assertEqual(self.calc.divide(0, 1), 0)
        self.assertIsNone(self.calc.divide(5, 0), "Division by zero should return None")

    def test_division_edge_cases(self):
        """Test division edge cases."""
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.3333333333333333, places=7)
        self.assertAlmostEqual(self.calc.divide(-1, 3), -0.3333333333333333, places=7)

if __name__ == "__main__":
    unittest.main()

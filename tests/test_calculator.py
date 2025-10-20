import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from calculator import MortgageCalculator

class TestMortgageCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calc = MortgageCalculator()
    
    def test_monthly_payment(self):
        payment = self.calc.calculate_monthly_payment(1000000, 7.5, 20)
        self.assertAlmostEqual(payment, 8059.99, places=1)
    
    def test_total_payment(self):
        total = self.calc.calculate_total_payment(1000000, 7.5, 20)
        self.assertAlmostEqual(total, 1934396.38, places=1)
    
    def test_total_interest(self):
        interest = self.calc.calculate_total_interest(1000000, 7.5, 20)
        self.assertAlmostEqual(interest, 934396.38, places=1)

if __name__ == '__main__':
    unittest.main()
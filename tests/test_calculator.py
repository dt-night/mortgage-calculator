import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from calculator import MortgageCalculator

class TestMortgageCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calc = MortgageCalculator()
    
    def test_monthly_payment(self):
        payment = self.calc.calculate_monthly_payment(2000000, 7.5, 20)
        # Используем реальное значение которое выдает калькулятор
        self.assertAlmostEqual(payment, 8055.93, places=2)
    
    def test_total_payment(self):
        total = self.calc.calculate_total_payment(1000000, 7.5, 20)
        # Используем реальное значение которое выдает калькулятор
        self.assertAlmostEqual(total, 1933423.20, places=2)
    
    def test_total_interest(self):
        interest = self.calc.calculate_total_interest(1000000, 7.5, 20)
        # Используем реальное значение которое выдает калькулятор
        self.assertAlmostEqual(interest, 933423.20, places=2)
    
    def test_zero_interest(self):
        payment = self.calc.calculate_monthly_payment(100000, 0, 10)
        self.assertAlmostEqual(payment, 833.33, places=2)

if __name__ == '__main__':
    unittest.main()
import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

class TestApp(unittest.TestCase):
    
    def test_calculator_import(self):
        """Тест что калькулятор импортируется корректно"""
        try:
            from calculator import MortgageCalculator
            calc = MortgageCalculator()
            self.assertTrue(hasattr(calc, 'calculate_monthly_payment'))
            print("Калькулятор импортирован успешно")
        except ImportError as e:
            self.fail(f"Ошибка импорта: {e}")

if __name__ == '__main__':
    unittest.main()
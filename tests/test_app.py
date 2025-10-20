import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestApp(unittest.TestCase):
    
    def test_file_existence(self):
        """Проверяем что основные файлы существуют"""
        self.assertTrue(os.path.exists('app.py'))
        self.assertTrue(os.path.exists('calculator.py'))
        self.assertTrue(os.path.exists('tests/test_calculator.py'))
    
    def test_calculator_import(self):
        """Проверяем что калькулятор импортируется"""
        try:
            from calculator import MortgageCalculator
            calc = MortgageCalculator()
            self.assertTrue(hasattr(calc, 'calculate_monthly_payment'))
            print("Калькулятор импортирован успешно")
        except ImportError as e:
            self.fail(f"Не удалось импортировать MortgageCalculator: {e}")

if __name__ == '__main__':
    unittest.main()
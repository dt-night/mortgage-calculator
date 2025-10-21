from calculator import MortgageCalculator

def main():
    """Основная функция приложения"""
    calculator = MortgageCalculator()
    
    print("КАЛЬКУЛЯТОР ИПОТЕКИ")
    print("Введите параметры кредита:")
    
    try:
        # Ввод данных
        principal = float(input("Сумма кредита (руб): "))
        annual_rate = float(input("Процентная ставка (% годовых): "))
        years = int(input("Срок кредита (лет): "))
        
        # Проверка валидности
        if principal <= 0 or annual_rate < 0 or years <= 0:
            print("Ошибка: введите положительные значения ")
            return
        
        # Расчет и вывод
        calculator.print_calculation(principal, annual_rate, years)
        
    except ValueError:
        print("Ошибка: введите числовые значения")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == '__main__':
    main()
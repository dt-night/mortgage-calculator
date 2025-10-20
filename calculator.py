class MortgageCalculator:
    """
    Простой калькулятор ипотеки для консоли
    """
    
    def calculate_monthly_payment(self, principal, annual_rate, years):
        """Расчет ежемесячного платежа"""
        monthly_rate = annual_rate / 100 / 12
        months = years * 12
        
        if monthly_rate == 0:
            return principal / months
        
        monthly_payment = (principal * monthly_rate * 
                         (1 + monthly_rate) ** months) / 
                         ((1 + monthly_rate) ** months - 1)
        
        return round(monthly_payment, 2)
    
    def calculate_total_payment(self, principal, annual_rate, years):
        """Расчет общей суммы выплат"""
        monthly_payment = self.calculate_monthly_payment(principal, annual_rate, years)
        return round(monthly_payment * years * 12, 2)
    
    def calculate_total_interest(self, principal, annual_rate, years):
        """Расчет общей суммы процентов"""
        total_payment = self.calculate_total_payment(principal, annual_rate, years)
        return round(total_payment - principal, 2)
    
    def print_calculation(self, principal, annual_rate, years):
        """Печать результатов расчета"""
        monthly = self.calculate_monthly_payment(principal, annual_rate, years)
        total = self.calculate_total_payment(principal, annual_rate, years)
        interest = self.calculate_total_interest(principal, annual_rate, years)
        
        print("\n" + "="*50)
        print("РАСЧЕТ ИПОТЕКИ")
        print("="*50)
        print(f"Сумма кредита: {principal:,.2f} руб.")
        print(f"Процентная ставка: {annual_rate}% годовых")
        print(f"Срок кредита: {years} лет")
        print("-"*50)
        print(f"Ежемесячный платеж: {monthly:,.2f} руб.")
        print(f"Общая сумма выплат: {total:,.2f} руб.")
        print(f"Переплата по процентам: {interest:,.2f} руб.")
        print("="*50)
from typing import Callable
import re

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

def generator_numbers(text: str):
    real_numbers = re.findall(" \d*\.\d{2} ", text)
    for numb in real_numbers:
        yield float(numb)
    
def sum_profit(text: str, func: Callable):
    sum = 0
    for profit in func(text):
        sum += profit
    return sum

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
import re
from typing import Callable
def generator_numbers(text:str):
   pattern = r'\s\d+(\.\d+)?'
   for match in re.finditer (pattern, text):
      yield match.group()

def sum_profit(text:str, func:Callable):
    return sum(func(num) for num in generator_numbers(text))
total_profit = sum_profit("Це текст 1.5 і 2.3",float)
print(total_profit)

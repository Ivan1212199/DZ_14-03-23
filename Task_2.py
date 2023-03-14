""""
Задача 2: Найдите сумму цифр трехзначного числа.

*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
"""

SumOfDigits = 123
print(SumOfDigits//100 + SumOfDigits//10%10 + SumOfDigits%10)
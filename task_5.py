print('Задача 5. Наибольшая сумма цифр')

# Вводится N чисел. 
# Среди натуральных чисел, которые были введены, 
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.

amount = int(input("Сколько чисел будет введено?\n"))
max_result = 0
max_sum = 0

for number in range(amount):
    number = input("Введите число: ")
    sum_number = 0
    for numerate in number:
        sum_number += int(numerate)
    if sum_number > max_sum:
        max_sum = sum_number
        max_result = int(number)
print(f'Наибольшее по сумме цифр число : {max_result}, сумма его цифр: {max_sum}')

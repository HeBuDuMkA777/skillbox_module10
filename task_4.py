print('Задача 4. Простые числа')

# Напишите программу, которая считает количество простых чисел в заданной последовательности и выводит ответ на экран.

# Простое число делится только на себя и на единицу. Последовательность задаётся при помощи вызова ввода (input) на каждой итерации цикла. Одна итерация — одно число.

# Пример:
# Введите количество чисел: 6.
# Введите число: 4.
# Введите число: 7.
# Введите число: 20.
# Введите число: 3.
# Введите число: 11.
# Введите число: 37.

# Количество простых чисел в последовательности: 4.

amount_num = int(input("Введите количество чисел: "))
prime_num_counter = 0

for _ in range(amount_num):
    is_prime = True
    my_num = int(input("Введите число: "))
    for divider in range(2, int(my_num ** 0.5) + 1):
        if my_num % divider == 0:
            is_prime = False
            break
    if is_prime:
        prime_num_counter += 1
print("Количество простых чисел в последовательности:", prime_num_counter)
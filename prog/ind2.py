#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == "__main__":
    list_1 = [5.0, 5.5, 3.5, 6.5, -8.0, 7.5, 7.0, -8.5, 9.0, 9.5]
    
    # Ввод числа C
    C = int(input("Введите значение для числа C:"))

    # Подсчёт количества элементов меньше C
    count = len([i for i in list_1 if i < C])
    
    # Определение индекса последнего отрицательного числа
    for i, item in enumerate(list_1):
        if (item < 0):
            last = i

    # Рачёт суммы после последнего отрицательного числа
    sum = 0
    for i, item in enumerate(list_1[last + 1:]):
        sum += int(item)
    
    # Вывод результатов
    print(f"Количество элементов меньше (C = {C}) = {count}")
    print(f"Сумма целых частей элементов списка: {sum}")
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == "__main__":
    list_1 = list(map(float, input().split()))
    
    # Ввод числа C
    C = int(input("Введите значение для числа C:"))

    # Подсчёт количества элементов меньше C
    count = len([i for i in list_1 if i < C])
    
    # Определение индекса последнего отрицательного числа
    for i, item in enumerate(list_1):
        if (item < 0):
            last = i

    # Рачёт суммы после последнего отрицательного числа
    print(sum)
    sum = sum([int(item) for i, item in enumerate(list_1) if i > last])
    
    # Вывод результатов
    print(f"Количество элементов меньше (C = {C}) = {count}")
    print(f"Сумма целых частей элементов списка: {sum}")
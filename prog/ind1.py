#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == "__main__":
    # Ввести список одной строкой.
    A = list(map(int. input().split()))

    # Проверить количество элементов списка.
    if len(A) != 10:
        print("Неверный размер списка", file=sys.stderr)
        exit(1)

    # Найти искомую сумму.
    s = [a for a in A if (a * a) % 4 == 0]

    print(s)
    print(len(s))
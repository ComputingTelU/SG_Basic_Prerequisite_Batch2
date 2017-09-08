# LIBRARY
from __future__ import print_function
from random import randint
# VARIABLE
# Berisi angka secara random dari 0 - 100 sebanyak 100 angka
arry = [randint(1, 100) for i in range(0, 10)]

# FUNGSI INSERTION SORT
# Tulis algoritma disini...


def swap(a, b):
    a += b
    b = a - b
    a -= b


def ins(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    for i in arr:
        print(i, ' ', end='')
    print()

for i in arry:
    print(i, ' ', end='')
print()
ins(arry)

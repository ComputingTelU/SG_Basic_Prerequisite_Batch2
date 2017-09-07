# LIBRARY
from random import randint

# VARIABLE
# Berisi angka secara random dari 0 - 100 sebanyak 100 angka
#arr = [randint(1,100) for i in range(0,100)]
def sort_numbers(s):
    for i in range(1, len(s)):
        val = s[i]
        j = i - 1
        while (j >= 0) and (s[j] > val):
            s[j+1] = s[j]
            j = j - 1
        s[j+1] = val

def main():
    x = eval(input("Enter numbers to be sorted: "))
    x = list(x)
    sort_numbers(x)
    print(x)
# FUNGSI INSERTION SORT
# Tulis algoritma disini...
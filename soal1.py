# LIBRARY
from random import randint

# VARIABLE
# Berisi angka secara random dari 0 - 100 sebanyak 100 angka
arr = [randint(1,100) for i in range(0,100)]

# FUNGSI INSERTION SORT
# Tulis algoritma disini...
def insertion(n):
    for i in range(1,len(n)):
        isidata = n[i]
        posisi = i
        while posisi > 0 and n[posisi-1]> isidata:
            n[posisi] = n[posisi-1]
            posisi = posisi-1
        n[posisi] = isidata

print (arr)
insertion(arr)
print (arr)
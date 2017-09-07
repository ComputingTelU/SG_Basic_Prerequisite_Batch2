# LIBRARY
from random import randint

# VARIABLE
# Berisi angka secara random dari 0 - 100 sebanyak 100 angka
arr = [randint(1,100) for i in range(0,100)]

def SelectionSort(val):
   for isi in range(len(val)-1,0,-1):
       Max=0
       for lokasi in range(1,isi+1):
           if val[lokasi]>val[Max]:
               Max = lokasi

       temp = val[isi]
       val[isi] = val[Max]
       val[Max] = temp
SelectionSort(arr)
print(arr)

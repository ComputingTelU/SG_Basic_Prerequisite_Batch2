# LIBRARY
from random import randint

# VARIABLE
# Berisi angka secara random dari 0 - 100 sebanyak 100 angka
array = [randint(1,100) for i in range(0,100)]

def ins_sort(k):
    for i in range(1,len(k)):   
        j = i                   
        while j > 0 and k[j] < k[j-1]: 
            k[j], k[j-1] = k[j-1], k[j]
            j=j-1 
    return k

ins_sort(array)
print(array)
# LIBRARY
from random import randint

# VARIABLE
# Berisi angka secara random dari 0 - 100 sebanyak 100 angka
arr = [randint(1,100) for i in range(0,100)]

# FUNGSI INSERTION SORT
# Tulis algoritma disini...
def insertion_sort(array):
	for i in range(1, len(array)):
		nilai = array[i]
		j = i - 1
		while (j>=0) and (array[j]>nilai):
			array[j+1] = array[j]
			j = j - 1
		array[j+1] = nilai

insertion_sort(arr)
for x in arr:
	print(x)
	
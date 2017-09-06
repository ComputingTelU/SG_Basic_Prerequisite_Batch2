# LIBRARY
from random import randint

# VARIABLE
# Berisi angka secara random dari 0 - 100 sebanyak 100 angka
arr = [randint(1,100) for i in range(0,100)]

# FUNGSI INSERTION SORT
# Tulis algoritma disini...
print(arr)
pass1 = 0
for pass1 in range(len(arr)-1):
	i = pass1 + 1
	temp = arr[i]
	while temp<arr[i-1] and i>0:
		arr[i] = arr[i-1]
		i = i-1
	arr[i] = temp

print("\nHasil Insertion Sort(Ascending) : ",arr)
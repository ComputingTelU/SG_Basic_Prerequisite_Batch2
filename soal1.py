# LIBRARY
from random import randint

# VARIABLE
# Berisi angka secara random dari 0 - 100 sebanyak 100 angka
arr = [randint(1,100) for i in range(0,100)]
#arr = [1,2,3,4,5,6,7,8,9,10]
# FUNGSI INSERTION SORT
def insertionSort(data):
	for i in range(len(data)):
		j = i-1
		temp = data[i]
		while (temp < data[j]) and (j >= 0):
			data[j+1] = data[j]
			j -= 1
		data[j+1] = temp
		

#MAIN PROGRAM	
print("Angka Acak 1-100 : ")
for i in arr:
	print(i, end=", ")
insertionSort(arr)
print("\n\nAngka Terurut : ")
for i in arr:
	print(i, end=", ")

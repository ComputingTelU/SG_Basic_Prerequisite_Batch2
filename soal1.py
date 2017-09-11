# LIBRARY
from random import randint

# VARIABLE
# Berisi angka secara random dari 0 - 100 sebanyak 100 angka
arr = [randint(1,100) for i in range(0,100)]
#arr = [7,5,4,2,1];

# FUNGSI INSERTION SORT
# Tulis algoritma disini...

#def insertionsort():
minimum=0
for i in range(1,len(arr)):
	#print(i)
	j=i-1
	minimum=arr[i]
	while(j>=0) and (arr[j]>minimum):
		arr[j+1]=arr[j]
		j-=1;
	arr[j+1]=minimum
#insertionsort()
#arr[0], arr[4]=arr[4], arr[0]
for each in arr:
	print(each),
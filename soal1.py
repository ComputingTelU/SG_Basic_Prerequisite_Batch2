#Insertion Short

# LIBRARY
from random import randint

# VARIABLE
# Berisi angka secara random dari 0 - 100 sebanyak 100 angka
arr = [randint(1,100) for i in range(0,100)]

# FUNGSI INSERTION SORT
# Tulis algoritma disini...
def insertionSort(list_input):
   for index in range(1,len(list_input)):

     currentvalue = list_input[index]
     position = index

     while position>0 and list_input[position-1]>currentvalue:
         list_input[position]=list_input[position-1]
         position = position-1

     list_input[position]=currentvalue
# TESTING
print(arr)
insertionSort(arr)
print(arr)

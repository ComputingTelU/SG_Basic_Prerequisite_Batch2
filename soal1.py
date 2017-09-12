# LIBRARY
from random import randint

# VARIABLE
# Berisi angka secara random dari 0 - 100 sebanyak 100 angka
arr = [randint(1,100) for i in range(0,100)]

# FUNGSI INSERTION SORT
# Tulis algoritma disini...
def insertionsort(list):                      #membuat prosedur insertionlist
	for i in range(1,len(list)):                #cek dari 1 sampai akhir
		angka = list[i]                           #ambil angka yang akan di bandingkan
		posisi = i                                #indeks posisi 
		while posisi>0 and angka<list[posisi-1]:  #cek bila sebelumnya lebih besar
			list[posisi]=list[posisi-1]             #geser 
			posisi=posisi-1
		list[posisi]=angka                        #kembalikan angka pembanding ke list
			

print(arr)                                    #cek sebelum berubah
insertionsort(arr)                            #urutkan
print(arr)                                    #cek sesudah berubah
#IF

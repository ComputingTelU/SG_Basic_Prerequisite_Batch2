# VARIABLE
# Sebagai inputan yang akan divalidasi
inputan = input("Masukkan: ")

# KELAS STACK
# Buatlah kelas objek Stack dengan 1 atribut yaitu array, lalu memiliki fungsi sbg berikut:
# isEmpty() -> return True jika Stack kosong dan False jika terisi.
# push(item) -> memasukkan item kedalam Stack
# pop() -> mengeluarkan item pada Stack
# size() -> menghitung jumlah item pada Stack
# printStack() -> output seluruh isi Stack
class Stack:

     def __init__(self):
          self.items = []  
     def isEmpty(self):
          return self.items == []  
     def push(self, item):
          self.items.append(item)  
     def pop(self):
          return self.items.pop()  
     def peek(self):
          return self.items[len(self.items)-1]  
     def size(self):
          return len(self.items)

# FUNGSI VALIDASI BRACKETS
# Tulis algoritma disini...

s = Stack()
#word = "()(()())"
i = 0;
for each in inputan:
	if(each == "("):
		s.push(each)
	elif(each == ")"):
		if(s.isEmpty()):
			break
		else:
			s.pop()
	i+=1;

if(s.isEmpty() and i==len(inputan)):
	print ("VALID")
else:
	print ("TIDAK VALID")
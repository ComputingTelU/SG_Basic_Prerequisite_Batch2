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

# FUNGSI VALIDASI BRACKETS
# Tulis algoritma disini...
class Stack:
	def __init__(self):
		self.items = []
		
	def isEmpty(self):
		return self.items == []
	def push(self, elm):
		return self.items.append(elm)
	def pop(self):
		if not self.isEmpty():
			return self.items.pop()
	def size(self):
		return len(self.items)
		
	def printStack(self):
		for i in self.items:
			print(i, end="")
		print()

#MAIN PROGRAM	
cek = True
buka = ["(", "{", "["]
tutup = [")", "}", "]"]
data = Stack()
i = 0
while (i< len(inputan)) and cek:
	if inputan[i] in buka: 
		data.push(inputan[i])

	elif inputan[i] in tutup:
		if data.isEmpty():
			cek = False
			break
		else:
			temp = data.pop()
			if inputan[i] == ")" and temp == "(":	
				cek = True
			elif inputan[i] == "}" and temp == "{":	
				cek = True
			elif inputan[i] == "]" and temp == "[":	
				cek = True
			else: cek = False
		
	i +=1		

if cek and data.isEmpty():
	print("Seimbang ")
else:
	print("Tidak Seimbang")

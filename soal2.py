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
	def size(self):
		return len(self.items)
	def printStack(self):
		return self.items[len(self.items)-1]


# FUNGSI VALIDASI BRACKETS
# Tulis algoritma disini...
def validation(inputan):
	stat = True
	s = Stack()
	for items in inputan:
		if items == '(':
			s.push(items)
		elif items == ')':
			if not s.isEmpty():
				s.pop()
			else:
				return False
	if not s.isEmpty():
		return False
	return stat

print(validation(inputan))

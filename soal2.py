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
    stacks = []

    def __init__(self, initialize = []):
        self.stacks = initialize

    def isEmpty(self):
        return self.stacks == []

    def push(self, item):
        self.stacks.append(item)

    def pop(self):
        return self.stacks.pop()

    def size(self):
        return len(self.stacks)

    def printStack(self):
        print(self.stacks)

# FUNGSI VALIDASI BRACKETS
# Tulis algoritma disini...
valid    = True
brackets = Stack()

for c in inputan:
    if not valid: break

    if   c == '(': brackets.push(1)
    elif c == ')':
        if not brackets.isEmpty(): brackets.pop()
        else: valid = False

if valid and not brackets.isEmpty(): valid = False

if valid:
    print("VALID!")
else:
    print("NOT VALID!")

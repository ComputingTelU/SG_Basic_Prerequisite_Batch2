from __future__ import print_function
# VARIABLE
# Sebagai inputan yang akan divalidasi
inputan = str(input("Masukkan: "))

# KELAS STACK
# Buatlah kelas objek Stack dengan 1 atribut yaitu array, lalu memiliki fungsi sbg berikut:
# isEmpty() -> return True jika Stack kosong dan False jika terisi.
# push(item) -> memasukkan item kedalam Stack
# pop() -> mengeluarkan item pada Stack
# size() -> menghitung jumlah item pada Stack
# printStack() -> output seluruh isi Stack


class Stack:
    def __init__(self):
        self.element = []

    def is_empty(self):
        return self.element

    def push(self, x):
        self.element.append(x)

    def pop(self):
        x = self.element.pop()
        return x

    def size(self):
        return len(self.element)

    def print_stack(self):
        for element in self.element:
            print(element,' ', end='')

    def cek_bracket(self):
        dmy = self.element
        pan = self.size()
        sum = 0
        cas = True
        for j in range(pan):
            x = dmy.pop()
            if x == '(':
                sum -= 1
            elif x == ')':
                sum +=1
            if sum < 0:
                cas = False
                break
        return cas

    def empty_element(self):
        self.element = []
# FUNGSI VALIDASI BRACKETS
# Tulis algoritma disini...

S = Stack()
for i in inputan:
    S.push(i)
print(S.cek_bracket())
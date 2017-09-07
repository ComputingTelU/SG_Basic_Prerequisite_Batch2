# LIBRARY
from random import randint

# VARIABLE
# Berisi angka secara random dari 0 - 100 sebanyak 100 angka
arr = [randint(1,100) for i in range(0,100)]

# FUNGSI INSERTION SORT
# Tulis algoritma disini...
print("Before:")
print(arr)
print()

class Sort:
    numbers = []

    def __init__(self, numbers):
        self.numbers = numbers

    def get(self):
        return self.numbers

    def insertion(self):
        numbers  = self.numbers
        length   = len(numbers)

        for i in range(1, length):
            cur = numbers[i]
            pos = i

            while pos > 0 and numbers[pos - 1] > cur:
                numbers[pos] = numbers[pos - 1]

                pos -= 1

            numbers[pos] = cur

sort = Sort(arr)
sort.insertion()

result = sort.get()

print("Result:")
print(result)

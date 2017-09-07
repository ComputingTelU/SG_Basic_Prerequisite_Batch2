# VARIABLE
# Sebagai inputan yang akan divalidasi
masukkan = ['(',')']
s = []

benar = "True"

for i in masukkan :
	if (i == '(') :
		s.append(i)
	elif (i == ')') :
		if (len(s) != 0):
			for j in s :
				if (j == '(') :
					s.remove(j)
					benar = "True"
					break
				elif (j != '(') :
					benar = "False"
					break
		elif (len(s) == 0) :
			benar = "False"
			break

if (len(s) != 0) :
	benar = "False"

print(s)
print(benar)
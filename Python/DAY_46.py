print("PROGRAM ANGKA GANJIL/GENAP".center(30,"="))

angka=int(input("Masukkan angka:"))
if angka %2 ==1:
	print(angka, "adalah angka ganjil")
else:
	print(angka, "adalah angka genap")
	
#atau dengan cara berikut:
	
print("PROGRAM ANGKA GANJIL/GENAP".center(30,"="))

angka=int(input("Masukkan angka:"))
if angka %2 ==0:
	print(angka, "adalah angka genap")
else:
	print(angka, "adalah angka ganjil")

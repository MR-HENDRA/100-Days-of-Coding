print("PROGRAM TAHUN KABISAT".center(30,"="))

def kabisat (n):
	if n % 400 == 0:
		return True
	elif n % 100 == 0:
		return False
	elif n % 4 == 0:
		return True
	else:
		return False

#tahun=2022 (juga bisa pakai cara ini)
	
tahun=int(input("Masukkan Tahun:"))

if kabisat(tahun):
		print (tahun, "adalah tahun kabisat")
else:
		print(tahun, "bukan tahun kabisat")
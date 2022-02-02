print("PROGRAM MENGHITUNG UMUR".center(30,"="))

nama=input("Masukkan Nama Kamu:")
tahun_lahir=int(input("Masukkan tahun lahir Kamu:"))
umur=2022-tahun_lahir

print(f"Hello {nama}, Saat ini kamu berusia {umur} tahun")
if umur>=12 and umur < 17:
	print("Kamu berada di masa Remaja Awal")
elif umur >=17 and umur < 26:
	print("Kamu  berada  di masa Remaja Akhir")
elif umur >= 26 and umur < 36:
	print("Kamu berada di masa Dewasa Awal")
elif umur >= 36 and umur < 46:
	print("Kamu berada di masa Dewasa Akhir")
elif umur >= 46:
	print("Kamu berada di masa lansia")
elif umur <1:
	print("Masukkan Tahun lahir dengan benar !")
else:
	print("Kamu masih Kanak-Kanak")
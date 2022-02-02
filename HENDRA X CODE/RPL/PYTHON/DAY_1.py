nilai = int(input("Masukkan nilai : "))

if nilai >= 90 and nilai <= 100:
    predikat = "A"
elif nilai >= 80 and nilai <= 89 :
    predikat = 'B'
elif nilai >= 70 and nilai <= 79 :
    predikat = 'C'
elif nilai >= 60 and nilai <= 69 :
    predikat = 'D'
else :
    print("Anda Tidak LULUS")

print('Nilai anda =', predikat)

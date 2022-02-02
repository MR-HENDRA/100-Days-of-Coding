#Contoh Soal

print("---------- TOKO SEMEN ABADI ----------")
hrg_semen = 50000
jumlah_semen = int(input("Jumlah Semen yang dibeli: "))
diskon1 = 2.5/100
diskon2 = 10/100
total = hrg_semen * jumlah_semen
if jumlah_semen >= 100 and jumlah_semen < 200 :
    diskon = total * diskon1
    hrg_Total = total - diskon
elif jumlah_semen >= 200 :
    diskon = total * diskon2
    hrg_Total = total - diskon
else:
    hrg_Total = total


print("Harga Total= Rp.",hrg_Total)
print("Silahkan Membayar sesuai dengan harga yang tertera\n")
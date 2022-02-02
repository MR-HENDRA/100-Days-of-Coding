print("========== HENDRA GAMING STORE ==========\n")
harga1paket=120000
jumlah_diamond=int(input("Masukkan Jumlah Paket Diamond dan Skin Legend:"))
print("Jumlah Unit yang dibeli:",jumlah_diamond)

if jumlah_diamond>=10 and jumlah_diamond<=19:
    print("Anda Mendapatkan diskon 20%")
    diskon=20/100
    
elif jumlah_diamond>=20 and jumlah_diamond<=49:
    print("Anda Mendapatkan diskon 30%")
    diskon=30/100
    
elif jumlah_diamond>=50 and jumlah_diamond<=69:
    print("Anda Mendapatkan diskon 35%")
    diskon=35/100
    
elif jumlah_diamond>=70 and jumlah_diamond<=99:
    print("Anda Mendapatkan diskon 40%")
    diskon=40/100

elif jumlah_diamond>=100:
    print("Anda Mendapatkan diskon 50%")
    diskon=50/100
   
else:
    print("Anda tidak Mendapatkan diskon !")
    diskon=0
       
harga_normal=harga1paket*jumlah_diamond
total_diskon=harga_normal*diskon
harga_total=harga_normal-total_diskon
hemat=harga_normal-harga_total

#print("Diskon yang didapat:",diskon)
print("Jumlah uang yang dihemat karena diskon:Rp. ",hemat)
print("Total Bayar:Rp. ",harga_total)
print("TERIMA KASIH TELAH TOP UP DI HENDRA GAMING STORE:)\n")

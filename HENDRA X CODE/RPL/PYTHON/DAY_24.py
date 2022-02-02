print("===== MENGHITUNG HARGA BERSIH PENJUALAN TANAH =====\n")
luas_tanah=int(input("Masukkan Luas Tanah:"))
harga_permeter=300000
total_harga=luas_tanah*harga_permeter
if total_harga>=50000000 and total_harga<100000000:
    print("Anda dikenakan pajak 3%")
    pajak=3/100
elif total_harga>=100000000:
    print("Anda dikenakan pajak 5%")
    pajak=5/100
else:
    print("Anda dikenakan pajak 1%")
    pajak=1/100
total_pajak=total_harga*pajak
harga_bersih=total_harga-total_pajak
print("Harga Bersih:", harga_bersih)
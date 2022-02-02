gaji=int(input("Masukkan Gaji perbulan:"))
if gaji >=10000000 and gaji <20000000:
    pajak=2/100
    total_pajak=pajak*gaji
    gaji_bersih=gaji-total_pajak
elif gaji >=20000000 :
    pajak=5/100
    total_pajak=pajak*gaji
    gaji_bersih=gaji-total_pajak
elif gaji <10000000:
    gaji_bersih=gaji

print("Total Gaji bersih : Rp. ",gaji_bersih)
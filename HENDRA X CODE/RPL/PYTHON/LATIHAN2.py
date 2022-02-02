pekerjaan=input("Masukkan Pekerjaan: ")
gaji=int(input("Masukkan Gaji Anda:"))
pajak1=2/100
pajak2=5/100
pajak_pns=3/100
if pekerjaan=='PNS':
    if gaji>=10000000 and gaji<20000000:
        pajak=pajak1+pajak_pns
        potongan=gaji*pajak
        gaji_bersih=gaji-potongan
    elif gaji>=20000000:
        pajak=pajak2+pajak_pns
        potongan=gaji*pajak
        gaji_bersih=gaji-potongan
    else:
        pajak=gaji*pajak_pns
        gaji_bersih=gaji-pajak
else:
    if gaji>=10000000 and gaji<20000000:
        pajak=pajak1
        potongan=gaji*pajak
        gaji_bersih=gaji-potongan
    elif gaji>=20000000:
        pajak=pajak2
        potongan=gaji*pajak
        gaji_bersih=gaji-potongan
    else:
        gaji_bersih=gaji
print("Gaji Bersih: Rp. ", gaji_bersih)
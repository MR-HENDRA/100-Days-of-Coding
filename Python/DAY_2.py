gaji_bulanan=5000000
pajak=2.5/100
ket_alpa=int(input("Masukkan Jumlah Ketidakhadiran (Tanpa Keterangan) Karyawan: "))
if ket_alpa > 5:
    potongan=25000*ket_alpa
    gaji_kotor=gaji_bulanan-potongan
    total_pajak=gaji_kotor*pajak
    gaji_bersih=gaji_kotor-total_pajak
else:
    total_pajak=gaji_bulanan*pajak
    gaji_bersih=gaji_bulanan-total_pajak

print("Gaji bulanan Karyawan: Rp.", gaji_bulanan)
print("Gaji Bersih Karyawan adalah Rp.", gaji_bersih)
#menyelesaikan contoh kasus
#gaji karyawan

nama=input("Masukkan Nama:")
anak=int(input("Masukkan Jumlah Anak:"))
gaji_pokok=int(input("Masukkan Gaji Pokok:"))

tunjangan_istri=20/100
tunjangan_anak=5/100*anak
total_tunjangan_istri=tunjangan_istri*gaji_pokok
total_tunjangan_anak=tunjangan_anak*gaji_pokok
total_tunjangan=total_tunjangan_istri+total_tunjangan_anak

gaji_kotor=gaji_pokok+total_tunjangan
pajak=10/100
total_pajak=gaji_kotor*pajak
gaji_bersih=gaji_kotor-total_pajak

print('\n\nNOTA GAJI KARYAWAN\n\n')
print('Nama: ', nama)
print('Tunjangan Istri: ', total_tunjangan_istri)
print('Tunjangan Anak: ', total_tunjangan_anak)
print('Total Tunjangan: ', total_tunjangan)
print('Total Gaji Kotor: ', gaji_kotor)
print('Total Pajak: ', total_pajak)
print('Total Gaji Bersih: ', gaji_bersih)




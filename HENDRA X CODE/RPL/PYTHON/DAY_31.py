print('===== MENGHITUNG GAJI KARYAWAN =====\n')
nama=input("Masukkan Nama Karyawan:")
gol=int(input("Masukkan Golongan Karyawan (1/2/3):"))

if gol==1:
    gaji=1500000
elif gol==2:
    gaji=1200000
elif gol==3:
    gaji=1000000
else:
    print('Masukkan Golongan dengan benar! opsi(1/2/3)')

tahun_sekarang=2022    
tahun_masuk_kerja=int(input("Masukkan Tahun Masuk Kerja Karyawan:"))
masa_kerja=tahun_sekarang-tahun_masuk_kerja

if masa_kerja>=7:
    bonus=150000
else:
    bonus=0
    
gaji_total=gaji+bonus

print(f'Masa Kerja Karyawan: {masa_kerja} tahun')  
print(f'Bonus:Rp.{bonus},00.') 
print(f'Gaji Total Karyawan:Rp.{gaji_total},00.')

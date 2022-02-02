#Menentukan Hari Berdasarkan Tanggal,Bulan,Tahun
#Dimulai Dari Monday(Senin) = 0 - Sunday(Minggu)= 6
print("PROGRAM MENENTUKAN HARI".center(30,"="))
import calendar
print(" ")
thn= int(input("Masukkan Tahun : "))
bln= int (input("Masukkan Bulan : "))
tgl= int(input("Masukkan Tanggal : "))
hari= calendar.weekday(thn,bln,tgl)
print(" ")
if hari== 0:
    print("Hari Pada Tanggal {} Bulan {} Tahun {} Adalah Senin".format(tgl,bln,thn))
if hari== 1:
    print("Hari Pada Tanggal {} Bulan {} Tahun {} Adalah Selasa".format(tgl,bln,thn))
if hari== 2:
    print("Hari Pada Tanggal {} Bulan {} Tahun {} Adalah Rabu".format(tgl,bln,thn))
if hari== 3:
    print("Hari Pada Tanggal {} Bulan {} Tahun {} Adalah Kamis".format(tgl,bln,thn))
if hari== 4:
    print("Hari Pada Tanggal {} Bulan {} Tahun {} Adalah Jumat".format(tgl,bln,thn))
if hari== 5:
    print("Hari Pada Tanggal {} Bulan {} Tahun {} Adalah Sabtu".format(tgl,bln,thn))
if hari== 6:
    print("Hari Pada Tanggal {} Bulan {} Tahun {} Adalah Minggu".format(tgl,bln,thn))
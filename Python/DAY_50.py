print("PROGRAM MENAMPILKAN KALENDER".center(30,"="))
print(" ")
import calendar
print(calendar.weekheader(3))
print(" ")
tahun=int(input("Masukkan Tahun:"))
bulan=int(input("Masukkan Bulan:"))
print(" ")
print("Kalender Pada Bulan {} tahun {} :".format(bulan,tahun))
print(" ")
print(calendar.month(tahun,bulan))

print("PROGRAM MENAMPILKAN KALENDER TAHUNAN".center(30,"="))
print(" ")
import calendar
print(" ")
tahun=int(input("Masukkan Tahun:"))
print(" ")
print("Kalender Pada tahun {} :".format(tahun))
print(" ")
print(calendar.calendar(tahun))
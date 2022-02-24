data_angka = [2,4,6,7,9,8,6,3,1,2,5,7,4,5,3,0,8,1,6,5]

print(f"data angka = {data_angka}")

# count data

jumlah_data_6 = data_angka.count(6) # mencari  jumlah data angka 6
jumlah_data_3 = data_angka.count(3) # mencari jumlah data angka 3
jumlah_data_5 = data_angka.count(5) # mencari jumlah data angka 5

print(f"jumlah data 6 = {jumlah_data_6}")
print(f"jumlah data 3 = {jumlah_data_3}")
print(f"jumlah data 5 = {jumlah_data_5}")

# ambil posisi data (index)

data = ["Hendra", "Usman", "Hendri", "Ali", "Fyan", "Ramadhan", "Arifatwa"]

print(f"data = {data}")

index_usman = data.index("Usman") # mencari posisi (index) data
index_ali = data.index("Ali")
print(f"index si Usman = {index_usman}")
print(f"index si Ali = {index_ali}")

# mengurutkan list
print(f"data angka sebelum sort = {data_angka}")
data_angka.sort()
print(f"data angka sort = {data_angka}")

print(f"data sebelum disort = {data_angka}")
data.sort()
print(f"data sort = {data}")

# balik listnya
data_angka.reverse()
data.reverse()
print(f"data direverse = {data_angka}")
print(f"data direverse = {data}")



# operasi

data = ["Hendra", "Fyan", "Ikhsan", "Andre", "Akmal"]

# mengambil data dari list
# cara simle
# print (data[0])

data_0 = data[0]
print(f"data pertama (index 0) = {data_0}")

data_terakhir = data [-1]
print(f"data terakhir = {data_terakhir}")

data_ikhsan = data[-3]
print(f"data ikhsan = {data_ikhsan}")

# mengambil info jumlah data dalam list
panjang_data=len(data)
print(f"panjang data = {panjang_data}")

## manipulasi data list

# menambahkan item dalam list pada item tertentu
print(f"data awal = \n{data}")

data.insert(1,"Arif")
print(f"data setelah ditambah = \n{data}")

# menambah di akhir list
data.append("Ryan")
print(f"data setelah ditambah = \n{data}")

# menambahkan list dengan list
data_baru = ["Hendri", "Adriawan", "Ainul"]
data.extend(data_baru)
print(f"data gabungan = \n{data}")

# merubah data
# kita ubah data 2 menjadi Ramadhan
data[2]= "Ramadhan"
print(f"data rubah = \n{data}")

# meremove data

data.remove("Akmal")
print(f"remove data = \n{data}")

# meremove data akhir

# data.pop()
# print(f"remove data paling akhir = \n{data}")

data_akhir = data.pop()
print(f"remove data akhir= \n{data}")
print(data_akhir)



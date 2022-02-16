print("Daftar Buah-buahan")
buah= [
    "Semangka", "Rambutan", "Durian", "Nangka", "Jambu", "Pepaya", "Langsat", "Manggis", "Pir", "Apel", "Anggur", "Jeruk", "Sirsak"
]

for i in buah :
    print(i)

cari_buah= input("Masukkan nama buah yang ingin dicari: ")
for i, buah in enumerate(buah):
    if buah.lower() == cari_buah.lower():
        print("Buah yang dicari terdapat pada indeks", i)
        break
else:
    print("Maaf buah yang anda cari tidak ada")

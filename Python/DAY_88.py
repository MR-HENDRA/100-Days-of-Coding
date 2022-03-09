# PROGRAM LIST BUKU

list_buku = []
while True:
    print("Masukkan Data Buku")
    judul = input("Masukkan Judul Buku\t:")
    penulis = input("Masukkan Nama Penulis\t:")

    buku_baru = [judul,penulis]
    list_buku.append(buku_baru)
    
    print("\n\n","="*10,"DATA BUKU","="*10)
    for index,buku in enumerate(list_buku):
        print(f"{index+1} |{buku[0]} | {buku[1]}")
        
    print("\n\n","="*20)
    lanjut = input("Next? (y/n) ")
    if lanjut == "n":
        break
    
print("PROGRAM SELESAI")
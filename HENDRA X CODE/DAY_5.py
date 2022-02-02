print("HENDRA CAFE")
menu = ["Es Jeruk","Es teh","Es Tebu"]
harga = [5000,3000,7000]
for i in menu:
    print(i)

pesanan = input("Masukkan Pesanan anda:")
pesanan.lower()
while pesanan != menu:
    if pesanan == 'Es Jeruk':
       print("Harga Es Jeruk =", harga[0])
       break
    elif pesanan == 'Es Teh':
        print("Harga Es Teh =", harga[1])
        break
    else :
        print("Masukkan pesanan sesuai list!")
        pesanan = input("Masukkan Pesanan anda:")
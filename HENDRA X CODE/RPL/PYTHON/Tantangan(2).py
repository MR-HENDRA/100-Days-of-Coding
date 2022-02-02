print("=============== HENDRA USMAN STORE ===============")

total_belanja = int(input("Masukkan total belanja : "))
kode_hari = input("Masukkan kode hari ini : ")
kode_hari = kode_hari.lower()
if kode_hari == "senin":
    discount = total_belanja*1/100
    print("Discount hari ini 1%")
elif kode_hari == "selasa":
    discount = total_belanja*2/100
    print("Discount hari ini 2%")
elif kode_hari == "rabu":
    discount = total_belanja*3/100
    print("Discount hari ini 3%")
elif kode_hari == "kamis":
    discount = total_belanja*4/100
    print("Discount hari ini 4%")
elif kode_hari == "jumat":
    discount = total_belanja*5/100
    print("Discount hari ini 5%")
elif kode_hari == "sabtu":
    discount = total_belanja*6/100
    print("Discount hari ini 6%")
elif kode_hari == "minggu":
    discount = total_belanja*7/100
    print("Discount hari ini 7%")
else:
   print("Kode hari anda salah")

pay = round(total_belanja - discount)
print("Jumlah discount : {}". format(discount))
print("Jumlah yang harus dibayar : {}". format(pay))
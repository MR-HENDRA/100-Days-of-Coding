print("===== PROGRAM MENGHITUNG KELILING PERSEGI DAN KONVERSI =====\n")

def meter(centimeter):
    result_meter = centimeter/100
    return result_meter

def persegi():
    result_persegi=meter(centimeter)*4
    print(result_persegi)

centimeter=int(input("Masukkan Panjang Sisi (dalam satuan Cm):"))
print(f'''Hasil Konversi dari {centimeter} Centimeter ke Meter adalah: {centimeter/100} m 
Hasil dari Keliling persegi (dalam satuan meter) adalah:''') 
persegi()



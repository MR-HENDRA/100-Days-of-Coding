print("===== MINAT ====\n")
print("Silahkan mengisi nilai mata pelajaran (angka 0-100)")
mtk=int(input("Masukkan Nilai MTK:"))
bing=int(input("Masukkan Nilai Bahasa Inggris:"))
bin=int(input("Masukkan Nilai Bahasa Indonesia:"))

skor=(mtk+bing+bin)/3

print("Pilihan Jurusan")
jurusan=['1. Elektro', '2. Mesin', '3. Pariwisata']
for i in jurusan:
    print(i)

minat=int(input("Masukkan Kode Minat Jurusan Anda:"))

if skor<70:
    print("Anda dinyatakan TIDAK LOLOS karena skor anda:", skor)
elif skor==70:
    if minat==1:
        jurusan="ELEKTRO"
    if minat==2:
        jurusan="MESIN"
    else:
        jurusan="PARIWISATA"
    print("Skor Anda adalah", skor, "Anda dinyatakan LOLOS ke bidang berikutnya:", jurusan)
elif skor>70 and skor<=100:
     print("Skor Anda adalah", skor, "Anda Bebas memilih jurusan yang disukai")   
    
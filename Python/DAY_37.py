print("===== PROGRAM MENGHITUNG IPK =====\n")
nama=input("Nama:")
nim=input("NIM:")
jumlah_mk=int(input("Jumlah Mata Kuliah:"))
print("====================\n")
nilai_mk=[]
total_sks=[]
for i in range(0,jumlah_mk):
    mk=input("Nama Mata Kuliah:")
    sks=int(input("Jumlah SKS:"))
    total_sks.append(sks)
    nilai=int(input("Nilai Mata Kuliah:"))
    if nilai>=80 and nilai<=100:
        nilai_mk.append(4*sks)
        print('Nilai huruf:A')
    elif nilai>=65 and nilai<=79:
        nilai_mk.append(3*sks)
        print('Nilai huruf:B')
    elif nilai>=55 and nilai<=64:
        nilai_mk.append(2*sks)
        print('Nilai huruf:C')
    elif nilai<55:
        nilai_mk.append(0*sks)
        print('Nilai huruf:D')
print("====================\n")
ipk=sum(nilai_mk)/sum(total_sks)
if ipk >=3.5 and ipk<=4:
    print("IPK=",ipk,' "PREDIKAT DENGAN PUJIAN"')
elif ipk >=3 and ipk<=3.49:
    print("IPK=",ipk,'"PREDIKAT SANGAT MEMUASKAN"')
elif ipk >=2.5 and ipk<=2.99:
    print("IPK=",ipk,'"PREDIKAT MEMUASKAN"')
elif ipk <2.5:
    print("IPK=",ipk,'"PREDIKAT LULUS"')


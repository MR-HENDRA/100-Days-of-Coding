print("====== MENGHITUNG BIAYA SPP SISWA ======\n")
nama=input("Masukkan Nama Lengkap:")
kelas=int(input("Masukkan Kelas:"))
pekerjaan=input("Masukkan Pekerjaan Orang Tua (PNS, Petani atau Wiraswasta):")
pekerjaan=pekerjaan.lower()

spp_normal=800000
pajak1=4/100
pajak2=6/100
pajak3=8/100
pajak_pns=1/100
diskon_petani=-1/100
diskon_wiraswasta=-0.5/100

if kelas==1:
    if pekerjaan=='pns':
        total_pajak=pajak1+pajak_pns
    elif pekerjaan=='petani':
        total_pajak=pajak1+diskon_petani
    elif pekerjaan=='wiraswasta':
        total_pajak=pajak1+diskon_wiraswasta
    else:
        total_pajak=0
        print("Masukkan pekerjaan ortu dengan benar. Masukkan input berupa: pns,petani atau wiraswasta")

elif kelas==2:
    if pekerjaan=='pns':
        total_pajak=pajak2+pajak_pns
    elif pekerjaan=='petani':
        total_pajak=pajak2+diskon_petani
    elif pekerjaan=='wiraswasta':
        total_pajak=pajak2+diskon_wiraswasta
    else:
        total_pajak=0
        print("Masukkan pekerjaan ortu dengan benar. Masukkan input berupa: pns,petani atau wiraswasta")

elif kelas==3:
    if pekerjaan=='pns':
        total_pajak=pajak3+pajak_pns
    elif pekerjaan=='petani':
        total_pajak=pajak3+diskon_petani
    elif pekerjaan=='wiraswasta':
        total_pajak=pajak3+diskon_wiraswasta
    else:
        total_pajak=0
        print("Masukkan pekerjaan ortu dengan benar. Masukkan input berupa: pns,petani atau wiraswasta")
else:
    total_spp=0
    print("Masukkan Kelas dengan Benar!")

biaya_pajak=spp_normal*total_pajak
total_spp=spp_normal+biaya_pajak

print('Biaya SPP yang harus kamu bayar adalah:Rp.',total_spp)
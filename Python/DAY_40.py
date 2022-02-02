#membuat fungsi sederhana
def jual_ayam():
    print('===== JUAL AYAM POTONG =====')

def harga_ayam():
    jual_ayam()
    print('Harga 1 Kg ayam adalah: Rp.20000')

#membuat fungsi dengan input argumen
def berat_ayam(kg):
    harga=20000
    harga_total=kg*harga
    print('Harga',kg, 'Kg ayam adalah: Rp.',harga_total)
#contoh
harga_ayam()
berat_ayam(2)
berat_ayam(5)

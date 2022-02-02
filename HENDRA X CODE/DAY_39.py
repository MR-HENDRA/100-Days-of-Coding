print('===== MENGHITUNG LUAS LINGKARAN =====')

def lingkaran(r):
    phi=3.14
    hasil=phi*r**2
    print('Luas Lingkaran adalah:', hasil)
lingkaran(2)

print('='*60)
print('===== MENGHITUNG LUAS LINGKARAN =====')


def luasLingkaran(diameter):
    phi = 3.14
    r = diameter/2
    luas = 2*phi*r
    return luas
diameter = int(input("Masukkan diameter : "))
print("Luas Lingkaran adalah : ",luasLingkaran(diameter))

def hitung(a,b,operasi):
    hasil=0
    if operasi=='tambah':
        hasil=a+b
    elif operasi=='kurang':
        hasil=a-b
    elif operasi=='kali':
        hasil=a*b
    elif operasi=='bagi':
        hasil=a/b
    return hasil

print(hitung(10,5,'tambah'))
print(hitung(10,5,'kurang'))
print(hitung(10,5,'kali'))
print(hitung(10,5,'bagi'))
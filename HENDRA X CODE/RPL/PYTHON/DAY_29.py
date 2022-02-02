#FUNGSI PADA LIST

#penambahan anggota
nama=['Hendra','Fyan','Merry','Naya','Parif']
nama=nama+['Rasul','Padli']
print(nama)

#penambahan anggota
nama.extend(['Arman','Feri'])
print(nama)

#penambahan anggota (Menyisipkan)
nama.insert(1,'Mikha')
print(nama)

#penambahan anggota (Menyisipkan)
nama[:0]=['Gibran']
print(nama)

#penghapusan anggota
del nama[2:]
print(nama)

#penghapusan anggota
nama.pop(0)
print(nama)

#penghapusan anggota
nama.remove('Hendra')
print(nama)
## Teknik mendupikat list

a = ["Hendra", "Usman", "Hendri", "Ali", "Fyan", "Ramadhan", "Arifatwa"]
print(f"a = {a}")

b = a # pass by reference
print(f"b = {b}")

# kita akan merubah elemen data pada a

a[0]= "Endang"
b.sort()
print(f"a = {a}")
print(f"b = {b}")

# addres dari kedua list a dan b
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")

# menduplikat list dengan copy
print("membuat list c dengan a.copy()")
c= a.copy() # full duplicat /  data baru

print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")
print(f"address c = {hex(id(c))}")

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")


print("Kita ubah data 0")
c[4]= "Endi"
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
# looping dari list

# for loop
print('\nFOR LOOP')
list_angka = [2,6,0,7,2,0,0,3]

for angka in list_angka:
    print(f"angka = {angka}")
    
anggota = ['Kk Heri','Kk Wiranto','Kk Zahra','Kk Aisyah','Arman','Rasul','Gibran','Parif','Fadli','Fyan','Hendra','Merry','Naya','Mikha']
    
for nama in anggota:
    print(f"nama = {nama}")

# for loop dan range
print('\nFOR LOOP AND RANGE')
kumpulan_angka = [0,8,0,3,2,0,2,2]

panjang = len(kumpulan_angka)

for i in range(panjang):
    print(f"angka = {kumpulan_angka[i]}")

# while
print('\nWHILE LOOP')
list_angka = [1,5,1,2,7,0]

panjang = len(kumpulan_angka)
i = 0

while i < panjang:
    print(f"angka = {kumpulan_angka[i]}")
    i += 1
    
# list comprehension 
print('\nLIST COMPREHENSION')
data = ['Hendra', 26,7,2003,'Usman']

[print(f"data={i}") for i in data]

angka2 = [1,5,1,2,7,0]

angka_kuadrat = [i**2 for i in angka2]
print(f"angka kuadrat = {angka_kuadrat}")

# enumerate
print('\nENUMERATE')
data_list = ['Hendra', 26,7,2003,'Usman']

for index, data in enumerate(data_list):
    print(f"index = {index}, data = {data}")



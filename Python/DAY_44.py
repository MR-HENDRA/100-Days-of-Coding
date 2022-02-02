print("ALGORITMA: INSERTION SORT".center(30,"="))
#mengurutkan dari kecil ke besar
list=[26,7,2003,31,12,1970,2018,2005,1973,9,2019,19]
print("Data yang akan di sort",list)
print("Insertion Sort :")
for j in range(len(list)-1,-1,-1):
    value=list[j]
    hole=j
    while hole <(len(list)-1) and list[hole+1]<list[hole]:
        list[hole] = list[hole+1]
        hole = hole+1
        list[hole] = value
print(list)

print('='*30)
def insertion(list):#Menggunakan def
    for j in range(len(list)-1,-1,-1):
        value = list[j]
        hole = j
        while hole <(len(list)-1) and list[hole+1]<list[hole]:
            list[hole] = list[hole+1]
            hole = hole+1
            list[hole] = value
    print(list)
list = [26,7,2003,31,12,1970,2018,2005,1973,9,2019,19]
print("Data yang akan di sort",list)
print("Insertion Sort :")
insertion(list)

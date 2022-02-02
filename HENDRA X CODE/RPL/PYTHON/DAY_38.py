print("===== MENGHITUNG LUAS SEGITIGA")

def step1(alas, tinggi):
    result_step1 = alas * tinggi
    return result_step1

def step2():
    result_step2 = step1(alas, tinggi)/2
    print (result_step2)

alas=int(input('Masukkan alas Segitiga:'))
tinggi=int(input('Masukkan tinggi segitiga:'))
print('luas segitiga adalah:')
step2()

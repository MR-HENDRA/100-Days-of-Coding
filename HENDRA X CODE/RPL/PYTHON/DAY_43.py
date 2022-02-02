print("ALGORITMA: BUBBLE SORT".center(30,"="))
#pada bubble sort ini kita menggunakan function def.
def sortir(x):
    for i in range(len(x)-1,0,-1):
        for j in range(i):
            if x[j]>x[j+1]:
                temp=x[j]
                x[j]=x[j+1]
                x[j+1]=temp

number=[26,7,2003,31,12,1970,2018,2005,1973,9,2019,19]
sortir(number)
print("Urutan dari data tersebut adalah:",number)

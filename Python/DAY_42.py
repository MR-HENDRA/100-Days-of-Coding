print("ALGORITMA: BUBBLE SORT".center(30,"="))
number=[26,7,2003,31,12,1970,2018,2005,1973,9,2019,19]
for i in range(len(number)-1,0,-1):
    for j in range(i):
        if number[j]>number[j+1]:
            temp=number[j]
            number[j]=number[j+1]
            number[j+1]=temp
print("Urutan dari data tersebut adalah:",number)

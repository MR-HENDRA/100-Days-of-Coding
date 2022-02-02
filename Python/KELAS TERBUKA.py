# pass, continue, and break.

#PASS -> berfungsi sebagai dummy, tidak akan dieksekusi

angka=0

#kondisi normal
while angka<5:
    angka+=1
    if angka==3:
        print('Hendra Ganteng Abizz!')
    print(angka)

#dengan pass
while angka<5:
    angka+=1
    if angka==3:
        pass # ini tidak akan dieksekusi
    print(angka)

#CONTINUE

angka=0
print(f"angka sekarang->{angka}")

while angka<5:
    angka+=1
    print(f"angka sekarang->{angka}")
    
    print("Hendra Gagah!")

print("Keren!\n")

angka=0
print(f"angka sekarang->{angka}")

while angka<5:
    angka+=1
    print(f"angka sekarang->{angka}")

    if angka ==3:
      print("Hendra Kece!")

    print("MY NAME IS HENDRA")
    
print("FINISH!\n")

angka=0
print(f"angka sekarang->{angka}")

while angka<5:
    angka+=1
    print(f"angka sekarang->{angka}") #aksi 1
    if angka ==3:
      print("Hendra Kece!")
      continue # akan membuat loop meloncat ke step selanjutnya

    print("MY NAME IS HENDRA") #aksi 2

print("FINISH!\n")

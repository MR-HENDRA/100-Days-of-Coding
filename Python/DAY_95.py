print("SELAMAT DATANG DI QUIZ INFORMATIKA !")

playing = input("Apakah Anda ingin bermain? key: (yes) ")

if playing.lower() != "yes":
    quit()

print("Okay! Ayo main:)")
score = 0

answer = input("Apa kepanjangan dari CPU? ")
if answer.lower() == "central processing unit":
    print('Benar!')
    score += 1
else:
    print('Salah!')

answer = input("Apa kepanjangan dari  GPU? ")
if answer.lower() == "graphics processing unit":
    print('Benar!')
    score += 1
else:
    print('Salah!')

answer = input("Apa kepanjangan dari RAM? ")
if answer.lower() == "random access memory":
    print('Benar!')
    score += 1
else:
    print('Salah!')

answer = input("Apa kepanjangan dari PSU? ")
if answer.lower() == "power supply":
    print('Benar!')
    score += 1
else:
    print('Salah!')

print("Anda menjawab " + str(score) + " pertanyaan dengan benar!")
print("Skor Anda " + str((score / 4) * 100))
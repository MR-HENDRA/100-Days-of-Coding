import turtle

turtle.bgcolor("black")
turtle.pensize(4)

def curve():
    for i in range (215):
        turtle.right(1)
        turtle.forward(1)

turtle.speed(1)
turtle.color('red','pink')

turtle.begin_fill()
turtle.left(145)
turtle.forward(110.80)
curve()

turtle.left(145)
curve()
turtle.forward(110.80)
turtle.end_fill()
turtle.hideturtle


#membuat fungsi sederhana
def jual_ayam():
    print('===== JUAL AYAM POTONG =====')

def harga_ayam():
    jual_ayam()
    print('Harga 1 Kg ayam adalah: Rp.20000')

#membuat fungsi dengan input argumen
def berat_ayam(kg):
    harga=20000
    harga_total=kg*harga
    print('Harga',kg, 'Kg ayam adalah: Rp.',harga_total)

harga_ayam()
berat_ayam(2)
berat_ayam(5)

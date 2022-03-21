print("MARI BERTARUNG DAN JADI PEMENANG !".center(30,"="))

player1 = {"nama":"Hendra","power":100}
player2 = {"nama":"Fyan","power":250}

def train(player):
    player["power"] += 100 # def latihan, untuk menambah power
    
def attack(attacker,defender):
    if(attacker["power"] > defender["power"]):
        print("Serangan berhasil! Kamu Hebat", attacker["nama"])
    else :
        print("Serangan Gagal! Kamu Lemah",attacker["nama"])

train(player1) # Latihan pertama player 1
train(player1) # Latihan kedua player 1
train(player2) # Latihan pertama player 2
train(player1) # Latihan kedua player 2
attack(player1,player2)


player1 = {"nama":"Fyan","power":100}
player2 = {"nama":"Hendra","power":250}

def train(player):
    player["power"] += 100 # def latihan, untuk menambah power
    
def attack(attacker,defender):
    if(attacker["power"] > defender["power"]):
        print("Serangan berhasil! Selamat untuk ", attacker["nama"])
    else :
        print("Serangan Gagal! Kamu Lemah ! ",attacker["nama"])

train(player1) # Latihan pertama
train(player1) # Latihan kedua
attack(player1,player2)

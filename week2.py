import random 

def angka_random():
    return random.randint(1,100)

def match_tebakan(angka_random,tebakan):
    hasil = False
    if angka_random == tebakan:
        print("selamat tebakan anda benar")
        hasil =True
    elif tebakan < angka_random:
        print("tebakan anda terlalu kecil")
    else:
        print("tebakan anda terlalu besar")
    
    return hasil
    



kesempatan = 5
angka_rand = angka_random()

while kesempatan >0:
    tebakan = int(input("masukan angka: "))
    
    if match_tebakan(angka_rand,tebakan):
        break

    kesempatan -=1

if kesempatan ==0:
    print("kesempatan habis")


    

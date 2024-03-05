"""
berat = 5412
ton = berat
kuintal = (berat % 1000)//100
#kuintal = (berat-(ton*1000))//100
kg = berat % 100
#kg = berat - (ton*1000)-(kuintal*100)
print (ton)
print (kuintal)
print (kg)
print ('\n')
if ton > 0:
    print (ton, 'ton')
if kuintal > 0:
    print (kuintal,'kuintal')
if kg > 0:
    print (kg, 'kg')
"""
import time
def count(total):

    list_konversi = ['Satu','Dua','Tiga','Empat','Lima','Enam','Tujuh','Delapan','Sembilan',"Se"]

    ratus_angka = total//100
    puluh_angka = (total % 100)//10
    satuan = total % 10
    konversi = ""

#output

    if ratus_angka > 0:
        if ratus_angka !=1:
            konversi = konversi + f"{list_konversi[ratus_angka-1]} ratus "
        else:
            konversi = konversi + f"{list_konversi[-1]}ratus "
    #print (f"{list_konversi[ratus_angka-1]}",'ratus')
    if puluh_angka > 1:
        konversi = konversi + f"{list_konversi[puluh_angka-1]} puluh "
    #print (f"{list_konversi[puluh_angka-1]}", 'puluh')

    
    if satuan >= 0:
        if (puluh_angka ==0 or puluh_angka > 1) and total %100 != 10 and satuan >0:
            konversi = konversi + f"{list_konversi[satuan-1]}"
    #print (f"{list_konversi[satuan-1]}", 'satuan')
        else:
            if total%100 != 10 :
                if satuan !=0:
                    if puluh_angka==1 and satuan ==1:
                        konversi = konversi + f"{list_konversi[-1]}belas"
                    else:
                        konversi = konversi + f"{list_konversi[satuan-1]} belas"
            else:
                konversi = konversi + "Sepuluh"
    print ('Terbilang adalah',konversi)

total = int(input())
count(total)


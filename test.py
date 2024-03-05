total = int(input("Masukan angka: "))
list_konversi = [
    "se",
    "dua",
    "tiga",
    "empat",
    "lima",
    "enam",
    "tujuh",
    "delapan",
    "sembilan"
]

ratus_angka = total //100
puluh_angka = (total%100)//10
satuan = total %10

konversi = ""

if ratus_angka >0:
    if ratus_angka != 1:
        konversi = konversi +f"{list_konversi[ratus_angka-1]} ratus "
    else:
        konversi = konversi +f"{list_konversi[ratus_angka-1]}ratus "

if puluh_angka >1:
    konversi = konversi +f"{list_konversi[puluh_angka-1]} puluh "

if satuan >=0:
    if puluh_angka>1 and total%100 != 10:
        konversi = konversi +f"{list_konversi[satuan-1]}"
    else:
        if total%100 != 10:
            if puluh_angka>1:
                konversi = konversi +f"{list_konversi[satuan-1]} belas"
            else:
                konversi = konversi +f"{list_konversi[satuan-1]}belas"
        else:
            konversi = konversi+" Sepuluh"

print(konversi)
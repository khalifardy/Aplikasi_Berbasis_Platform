import datetime as dt 

skrng = dt.datetime.now().year

tahun = int(input("Masukan tahun kelahiran anda: "))
plat = input("Masukan plat nomor: ")
print("===============================")
list_nomor_Plat = []

string_nomor_plat = ""
for i in plat:
    try:
        int(i)
        string_nomor_plat += i
    except:
        pass


genap = False
if int(string_nomor_plat)%2 == 0:
    genap = True

umur = skrng - int(tahun)
print(f"Tahun ini usia anda {umur} tahun")
print("nomor plat anda adalah "+string_nomor_plat)

if umur >= 17 and umur <= 45:
    if genap:
        print(
            "Kategori Plat nomor anda adalah genap\n",
            "Anda boleh mengurus STNK"
        )
    else:
        print(
            "Kategori Plat nomor anda adalah ganjil\n",
            "Anda Tidak boleh mengurus STNK"
        )

else:
    print("umur anda tidak diatas 17 dan dibawah 45 tahun\n","Anda Tidak boleh mengurus STNK")
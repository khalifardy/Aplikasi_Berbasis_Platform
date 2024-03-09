import datetime as dt

def input_nama():
    nama = input("masukan nama : ")
    if nama.replace(" ", "").isalpha():
        if len(nama) < 20:  # Mengizinkan spasi dalam nama tapi memastikan sisanya adalah huruf
            return nama
        else:
            print("nama harus kurang dari 20")
            return input_nama()
    else:
        print("Nama hanya boleh berisi huruf. Silakan coba lagi.")
        return input_nama()


def input_judul_buku():
    judul = input("masukan jdul buku: ")
    return judul

def input_tanggal():
    tanggal = input("masukan tanggal: ")
    try:
        tgl = dt.datetime.strptime(tanggal,"%d/%m/%Y")
        return tgl
    except:
        print("format tanggal tidak sesuai")
        return input_tanggal()

def keanggotaan():
    anggota = input("Sdah menjadi anggota : ")
    if anggota.lower() not in ["y","n",'yes',"no"]:
        print("input tidak sesuai: ")
        return keanggotaan()
    return anggota
        


print("Silahkan Isi  Untuk Pemimjaman buku : ")

nama = input_nama()
judul = input_judul_buku()
tanggal = input_tanggal()
anggota = keanggotaan()

print(" ")
print(f"Nama : {nama}")
print(f"Judul Buku: {judul}")
print("Tanggal Pemimjaman : {}".format(tanggal.strftime("%d-%m-%Y")))
print(f"Anggota: {anggota}")
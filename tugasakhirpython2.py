'''
Tugas Akhir Diklat Pemrograman Python
Aplikasi Gudang Sayur dan Buah
Oleh : Fatichatus Istighfarini
'''

import os
import csv
def home():
    pilihan_menu = daftar_menu()

    if (pilihan_menu == 1):
        data_masuk()
    elif (pilihan_menu == 2):
        show_data()
    elif (pilihan_menu == 3):
        judul = 'Daftar_Sayur_Maret_2024.csv'
        row = input('data yang ingin dihapus: ')
        hapus_data(int(row)-1,judul)
        #print (show_data())
    elif (pilihan_menu == 4):
        print ('Sampai jumpa kembali')

def back_menu():
    back_menu=input('Ketik Y untuk kembali ke menu utama')
    if(back_menu.lower()=='y'):
        home()
    else:
        print("Terima kasih sudah menggunakan Program")

def daftar_menu():
    print ('Menu')
    print ('1. Masukkan Data')
    print ('2. Tampilkan Data')
    print ('3. Hapus Data')
    print('4. Keluar Aplikasi')

    pilihan_menu = int(input('Masukkan pilihan angka menu:'))
    try:
        return pilihan_menu 
    except:
        print ('Gagal Kembali')

def data_masuk():
    pilihan_input ='y'
    while (pilihan_input=='y'):
        daftar_sayur()
        pilihan_input=input('Apakah ada data lain yang akan dimasukkan? (y/t)')

        if (pilihan_input.lower() !='y'):
            home()
            break
def daftar_sayur():
    sayur=[]
    nama_sayur = input ('Nama :')
    
    while True:
        try:
            harga = int(input ('Harga :'))
            break
        except ValueError:
            print('Masukkan harus dalam bentuk angka')
    
    kualitas = input ('Grade :')
    sayur.append([nama_sayur,harga,kualitas])
    print(sayur)

    
    with open('Daftar_Sayur_Maret_2024.csv', 'a',newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(sayur)
        csvfile.close()

    print ('Data diterima')


def show_data():
    print('Daftar Sayur')
    print("================================")

    with open ('Daftar_Sayur_Maret_2024.csv','r') as file:
        rows = []
        data = csv.reader(file)
        for row in data:
            print('Nama :',row[0])
            print('Harga (per kg) :',row[1])
            print ('Grade :',row[2])
            print('===================================')
    
    back_menu()

def hapus_data(row,judul):
    nama_file = judul
    indeks_row_yang_dihapus = row  


    data_baru = []
    with open(nama_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for indeks, row in enumerate(reader):
            if indeks != indeks_row_yang_dihapus:
                data_baru.append(row)


    with open(nama_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data_baru)
    
    print("data berhasil dihapus")
    back_menu()


if __name__ == '__main__':
   home()
        



from asyncore import loop
from cmath import e
import os


while loop:

    def menu():
        print("\n===============================")
        print("Program Booking Villa Puncak Bogor")
        print("===============================")
        print("1. Cipanas, Bogor")
        print("2. Cisarua, Bogor")
        print("3. Megamendung, Bogor")
        print("4. Gagod, Bogor")
        print("5. Exit")
        print("\n===============================")

    def pesan():
        jmlh_Booking = int(input("Masukan jumlah Booking (cth: 1): "))
        num_array = list()
        num = input("Berapa orang yang ingin menginap ? : ")
        print("Masukan nama penginap : ")
        for i in range(int(num)):
            i += 1
            n = input("orang ke {} :".format(i))
            num_array.append(str(n))
        total_Booking = jmlh_Booking * harga
        os.system("cls")
        print("\n----------------------------------------------")
        print("Anda telah berhasil melakukan booking villa ")
        print("----------------------------------------------")
        print("Nama Pemesan :".format(len(num_array)))
        for a in num_array:
            print(("- {}").format(a))
        print("Total Harga", "Rp.", (total_Booking))

    menu()
    tujuan = int(input("Masukan Pilihan [1-5] : "))

    if (tujuan) == 1:
        print("\n-------------------------------------------------------")
        print("\nKode  Nama\tKota\t\tHarga")
        print("\n      Villa\tTujuan\t\tBooking/malam")
        print("\n-------------------------------------------------------")
        print("\n101.  Giri\tCipanas \tRp. 300.000")
        print("\n102.  Sofia\tCipanas \tRp. 500.000")
        print("\n103.  Sabrina\tCipanas \tRp.700.000")
        print("\n-------------------------------------------------------")
        no_villa = int(input("Masukan kode villa : "))

        if (no_villa) == 101:
            harga = 300000
            print("")
            print("---------------------------------")
            print("Anda memilih kode villa", +int(no_villa))
            print("---------------------------------")
            pesan()

        elif (no_villa) == 102:
            harga = 500000
            print("")
            print("---------------------------------")
            print("anda memilih kode villa", +int(no_villa))
            print("---------------------------------")
            pesan()

        elif (no_villa) == 103:
            harga = 700000
            print("")
            print("---------------------------------")
            print("anda memilih kode villa", +int(no_villa))
            print("---------------------------------")
            pesan()

        else:
            os.system("cls")
            print("kode villa tidak ada dalam daftar")

    elif (tujuan) == 2:
        print("\n----------------------------------------------------------")
        print("\nKode  Nama\tKota\t\tHarga")
        print("\n      villa\tTujuan\t\tBooking/malam")
        print("\n----------------------------------------------------------")
        print("\n201. Masada\tCisarua \tRp. 320.000")
        print("\n202. Nirvana\tCisarua \tRp. 400.000")
        print("\n203. Jasmine\tCisarua \tRp. 420.000")
        print("\n----------------------------------------------------------")
        no_villa = int(input("Masukan kode villa :"))

        if (no_villa) == 201:
            harga = 320000
            print("")
            print("---------------------------------")
            print("Anda memilih kode villa", +int(no_villa))
            print("---------------------------------")
            pesan()

        elif (no_villa) == 202:
            harga = 400000
            print("")
            print("---------------------------------")
            print("Anda memilih kode villa", +int(no_villa))
            print("---------------------------------")
            pesan()

        elif (no_villa) == 203:
            harga = 420000
            print("")
            print("---------------------------------")
            print("Anda memilih kode villa", +int(no_villa))
            print("---------------------------------")
            pesan()
            e
        else:
            os.system("cls")
            print("Kode villa tidak ada dalam daftar")

    elif (tujuan) == 3:
        print("\n-------------------------------------------------------")
        print("\nKode  Nama\tKota\t\tHarga")
        print("\n      villa\tTujuan\t\tBooking")
        print("\n-------------------------------------------------------")
        print("\n301. BatuTua\tMegamendung \tRp. 310.000")
        print("\n302. Vimala\tMegamendung\tRp. 400.000")
        print("\n303. Shambala\tMegamendung \tRp.470.000")
        print("\n-------------------------------------------------------")
        no_villa = int(input("Masukan kode villa :"))

        if (no_villa) == 301:
            harga = 310000
            print("")
            print("---------------------------------")
            print("Anda memilih kode villa", +int(no_villa))
            print("---------------------------------")
            pesan()

        elif (no_villa) == 302:
            harga = 400000
            print("")
            print("---------------------------------")
            print("Anda memilih kode villa", +int(no_villa))
            print("---------------------------------")
            pesan()

        elif (no_villa) == 303:
            harga = 470000
            print("")
            print("---------------------------------")
            print("Anda memilih kode villa", +int(no_villa))
            print("---------------------------------")
            pesan()

        else:
            os.system("cls")
            print("Kode villa tidak ada dalam daftar")

    elif (tujuan) == 4:
        print("\n-------------------------------------------------------")
        print("\nKode  Nama\tKota\t\tHarga")
        print("\n      villa\tTujuan\t\tBooking")
        print("\n-------------------------------------------------------")
        print("\n401. ArgoPuro\tGadog \tRp. 390.000")
        print("\n403. Lavender\tGadog \tRp. 435.000")
        print("\n-------------------------------------------------------")
        no_villa = int(input("Masukan kode villa :"))

        if (no_villa) == 401:
            harga = 390000
            print("")
            print("---------------------------------")
            print("Anda memilih kode villa", +int(no_villa))
            print("---------------------------------")
            pesan()

        elif (no_villa) == 402:
            harga = 395000
            print("")
            print("---------------------------------")
            print("Anda memilih kode villa", +int(no_villa))
            print("---------------------------------")
            pesan()

        elif (no_villa) == 403:
            harga = 435000
            print("")
            print("---------------------------------")
            print("Anda memilih kode villa", +int(no_villa))
            print("---------------------------------")
            pesan()

        else:
            os.system("cls")
            print("Kode villa tidak ada dalam daftar")

    elif (tujuan) == 5:
        os.system("cls")
        exit()

    else:
        os.system("cls")
        print("***Pilihan tidak ada dalam daftar***")

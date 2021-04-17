import datetime
import random

def platnomor():
    angka1 = random.randint(1000, 9999)
    depan = random.choice(["A", "B", "C", "D", "E", "F",
                           "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R"])
    blkg = random.choice(["AV", "BD", "CK", "DS", "ET", "FN",
                          "GD", "HL", "IQ", "JY", "KE"])

    return print(f"Plat Nomor      : {depan} {angka1} {blkg}")


def bukti_transaksi(nama, alamat, selected, pay):
    x = datetime.datetime.now()
    Bulan = x.strftime("%B")
    hari = x.strftime("%A")
    tanggal = x.strftime("%d")
    tahun = x.strftime("%Y")
    jam = x.strftime("%X")
    print("======== BUKTI TRANSAKSI ========")
    print(f"Nama            : {nama}")
    print(f"Alamat          : {alamat}")
    print(f"Mobil           : {selected}")
    platnomor()
    print(f"Pembayaran      : {pay}")
    print(f"waktu Pembelian : {hari}, {tanggal} {Bulan} {tahun} , {jam}")
    print("=================================")
    print("------ Transaksi Berhasil -------")
    print("Mobil Anda Akan Dikirim dalam 1x24 Jam")


def Transaksi(selected):
    nama = input("Nama      : ")
    alamat = input("Alamat    : ")
    back2 = "y"
    while back2 == "y":
        print("1. Cash")
        print("2. Kredit")
        pay = int(input("Pilih Metode Pembayaran : "))
        if pay == 1:
            pay = "Cash"
            bukti_transaksi(nama, alamat, selected, pay)
            back2 = "n"
        elif pay == 2:
            pay = input("Jangka waktu : ")
            bukti_transaksi(nama, alamat, selected, pay)
            back2 = "n"
        else:
            print("Pilih 1 - 2!!!")


class car:
    def __init__(self, showroom):
        self.showroom = showroom

    def bmw(self, brand):
        back1 = "y"
        while back1 == "y":
            print(
                f" ======================== {brand} ========================")
            print(
                f"| 1. {brand} M8 Competition Coupe      - Rp 7.700.000.000  |")
            print(
                f"| 2. {brand} 320i                      - Rp 976.000.000    |")
            print(
                f"| 3. {brand} X7                        - Rp 2.611.000.000  |")
            print(
                f"| 4. {brand} 840i Coupe                - Rp 2.837.000.000  |")
            print(f" ======================================================== ")

            car = int(input("Pilih Mobil Yang Anda Inginkan : "))

            if 1 <= car <= 4:
                car_selected = {
                    1: f"{brand} M8 Competition Coupe",
                    2: f"{brand} 320i",
                    3: f"{brand} X7",
                    4: f"{brand} 840i Coupe"
                }
                selected = "%s" % car_selected.setdefault(car)
                print(
                    f"Mobil Yang Anda Pilih Adalah {selected}, Silahkan Isi Formulir Registrasi : ")
                Transaksi(selected)
                back1 = "n"
            else:
                print("Input 1-4")

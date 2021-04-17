import sh_method


def main_brand(showroom):
    print(f" ==== WELCOME TO {showroom} ====")
    print("| 1. BMW                         |")
    print("| 2. BUGATTI                     |")
    print("| 3. LAMBORGHINI                 |")
    print("| 4. FERRARI                     |")
    print(" ================================")


objek = sh_method.car("Prestigecars")
back = "y"
while back == "y":
    main_brand("Prestigecars")
    menu = (input("Pilih Brand Mobil Yang Anda Inginkan : "))
    if menu == "1":
        brand = "BMW"
        objek.bmw(brand)
        back = input("kembali ke menu ? y/n :")
    elif menu == "2":
        brand = "BUGATTI"
        objek.Bugatti(brand)
        back = input("kembali ke menu ? y/n :")
    elif menu == "3":
        brand = "LAMBORGHINI"
        objek.Lamborghini(brand)
        back = input("kembali ke menu ? y/n :")
    elif menu == "4":
        brand = "FERRARI"
        objek.Ferrari(brand)
        back = input("kembali ke menu ? y/n :")
    else:
        print("Input 1-4")
print("Terima Kasih Telah Mengunjungi Prestigecars")

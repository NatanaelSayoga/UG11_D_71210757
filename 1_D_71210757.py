benang = input("Masukkan string: ")
def cekString(benang):
    try:
        bulat = int(benang)
        if bulat % 2 == 0:
            print(bulat/2)
        else:
            print((bulat+5)/2)
    except ValueError:
        try:
            desimal = float(benang)
            if (int(desimal)) % 2 == 0:
                print(int(desimal) / 2)
            else:
                print((int(desimal) + 5) / 2)
        except ValueError:
                print(benang[::-1])
cekString(benang)
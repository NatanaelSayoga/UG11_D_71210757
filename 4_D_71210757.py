num1 = 4
num2 = 2
num3 = 6
masukkan_pertama = [0,1,2]
masukkan_kedua = [0,1,2]
masukkan_ketiga = [0,1,2]
jumlah_percobaan = 1
mulai = int(input("untuk memulai program masukkan (-1) untuk mulai : "))

def tabakangka(num1, num2, num3, jumlah_percobaan):
    print("Apakah " + str(num1) +
          "?\nApakah tebakan sudah benar ? "
          "\nLebih kecil (0)"
          "\nLebih besar (1)"
          "\nBenar (2) \n" + input(masukkan_pertama(": ")))
    if masukkan_pertama == 2:
        print("hasil penjumlahannya pasti " + str(num1) + "!\n jumlah tebakan : " + str(jumlah_percobaan) + "program selesai")
    elif masukkan_pertama == 0:
        print("Apakah " + str(num2) +
              "?\nJumlah tebakan: 2"
              "\nApakah tebakan sudah benar ? "
              "\nLebih kecil (0)"
              "\nLebih besar (1)"
              "\nBenar (2) \n" + input(masukkan_kedua(": ")))
        if masukkan_kedua == 2:
            print("hasil penjumlahannya pasti " + str(num2) + "!\n jumlah tebakan : " + str(2) + "program selesai")
        elif masukkan_kedua == 0:
            print("Hasil penjumalhannya pasti " + str(1) +
                  "?\nJumlah tebakan: 3 \nProgram selesai")
        else:
            print("Hasil penjumalhannya pasti " + str(3) +
                  "?\nJumlah tebakan: 3"
                  "\nProgram selesai")
    else:
        print("Apakah " + str(num3) +
              "?\nJumlah tebakan: 2"
              "\nApakah tebakan sudah benar ? "
              "\nLebih kecil (0)"
              "\nLebih besar (1)"
              "\nBenar (2)\n" + input(masukkan_kedua(": ")))
        if masukkan_kedua == 2:
            print("hasil penjumlahannya pasti " + str(num3) + "!\n jumlah tebakan : " + str(2) + "program selesai")
        elif masukkan_kedua == 0:
            print("Hasil penjumalhannya pasti " + str(5) +
                "?\nJumlah tebakan: 3"
                "\nProgram selesai")
        else:
            print("Hasil penjumalhannya pasti " + str(7) +
            "?\nJumlah tebakan: 3"
            "\nProgram selesai")

if mulai != -1:
    print("Program tidak berhasil dijalankan")
else:
    tabakangka(num1, num2, num3, jumlah_percobaan)
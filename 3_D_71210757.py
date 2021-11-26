import random
mulai = input("Masukkan tipe yang ingin anda coba : ")
truemul = mulai.lower()
perbandingan = ['<', '>', '==']
operasi = ['+', '-']
def generatesoal():
    global soal, num1, num2, num3, num4
    soal = random.choice(perbandingan)
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    num3 = random.randint(1, 20)
    num4 = random.randint(1, 20)
    if truemul == "penjumlahan":
        soal1 = (str(num1) + "+" + str(num2) + random.choice(perbandingan) + str(num3) + "+" + str(num4))
        print("(benar/salah) jika", soal1)
    elif truemul == "pengurangan":
        soal2 = (str(num1) + "-" + str(num2) + random.choice(perbandingan) + str(num3) + "-" + str(num4))
        print("(benar/salah) jika", soal2)
    else:
        print("something went wrong")
generatesoal()

jawaban = input("Masukkan jawaban Anda : ")
truejaw = jawaban.lower()
if truejaw == "benar":
    truejaw = True
elif truejaw == "salah":
    truejaw = False
else:
    print("something went  wrong")
def cekHasil(soal, truejaw):
    jum1 = num1 + num2
    jum2 = num3 + num4
    kur1 = num1 - num2
    kur2 = num3 - num4
    pembanging1 = bool(jum1 == jum2)
    pembanging2 = bool(kur1 == kur2)
    kurang1 = bool(jum1 < jum2)
    kurang2 = bool(kur1 < kur2)
    lebih1 = bool(jum1 > jum2)
    lebih2 = bool(kur1 > kur2)
    if truemul == "penjumlahan" and soal == "==":
        if pembanging1 == truejaw:
            print("Jawaban Anda benar !")
        else:
            print("Jawaban Anda masih salah !")
    elif truemul == "penjumlahan" and soal == "<":
        if kurang1 == truejaw:
            print("Jawaban Anda benar !")
        else:
            print("Jawaban Anda masih salah !")
    elif truemul == "penjumlahan" and soal == ">":
        if lebih1 == truejaw:
            print("Jawaban Anda benar !")
        else:
            print("Jawaban Anda masih salah !")
    elif truemul == "pengurangan" and soal == "==":
        if pembanging2 == truejaw:
            print("Jawaban Anda benar !")
        else:
            print("Jawaban Anda masih salah !")
    elif truemul == "pengurangan" and soal == "<":
        if kurang2 == truejaw:
            print("Jawaban Anda benar !")
        else:
            print("Jawaban Anda masih salah !")
    elif truemul == "pengurangan" and soal == ">":
        if lebih2 == truejaw:
            print("Jawaban Anda benar !")
        else:
            print("Jawaban Anda masih salah !")
cekHasil(soal,truejaw)
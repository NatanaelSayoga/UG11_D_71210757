benang = input("Masukkan sebuah kata/kalimat : ")
karakter = input("masukkan karakter yang ingin disisipkan : ")
truechar = " " + str(karakter) + " "
def sisipHuruf(benang):
    huruf = list(benang.upper())
    hurufpisah = tuple(huruf)
    pisahjadi = truechar.join(hurufpisah)
    print(pisahjadi)
def sisipKata(benang):
    kata = benang.split()
    katapisah = tuple(kata)
    katajadi = truechar.join(katapisah)
    print(katajadi)
sisipHuruf(benang)
sisipKata(benang)
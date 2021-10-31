import random

def masterminddef():
    try:
        kullanici_sayisi = int(input("10 ile 98 arasinda bir sayi gir"))
        if not 10<kullanici_sayisi<98:
            masterminddef()
        return kullanici_sayisi
    except:
        print("lütfen doğru rakam girin")
        masterminddef()

bilgisayar_sayisi = random.randint(10,98)
kullanici_number = 0
dogru = 0
yanlis = 0
mastermind = True
kullanici_sayisi = masterminddef()
while mastermind:
    while str(bilgisayar_sayisi)[0] == str(bilgisayar_sayisi)[1]:
        bilgisayar_sayisi = random.randint(10, 98)
    while kullanici_sayisi != bilgisayar_sayisi:
        kullanici_sayisi = masterminddef()
        if str(kullanici_sayisi)[0] == str(bilgisayar_sayisi)[0]:
            dogru+=1
        elif str(kullanici_sayisi)[1] == str(bilgisayar_sayisi)[1]:
            dogru+=1
        elif str(kullanici_sayisi)[0] != str(bilgisayar_sayisi)[0]:
            yanlis+=1
        elif str(kullanici_sayisi)[1] != str(bilgisayar_sayisi)[1]:
            yanlis+=1
        if kullanici_sayisi==bilgisayar_sayisi:    
            print("dogru sayiyi buldunuz")
            print("bilgisayarin sayisi {} idi".format(bilgisayar_sayisi))
            print("arti puaniniz{} /eksi puaniniz{}".format(dogru,yanlis))

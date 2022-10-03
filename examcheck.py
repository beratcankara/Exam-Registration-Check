import os
a = True
class deneme():
    def __init__(self,turk,math,social,scnc):
        self.math = math
        self.turk = turk
        self.social = social
        self.scnc = scnc
    
    def kontrol(self):
        if self.math > 41 or self.turk > 41 or self.social > 20 or self.scnc > 20:
            print("Hatalı sonuçlar girdiniz lütfen tekrar giriniz.")
            global a
            a = False
        if self.turk < 25:
            print("Türkçe netiniz az, çalışmalısınız.")
        if self.math < 25:
            print("Matematik netiniz az, çalışmalısınız.")
        if self.social < 15:
            print("Sosyal netiniz az, çalışmalısınız.")
        if self.scnc < 15:
            print("Fen netiniz az, çalışmalısınız.")
def yazdir(self):
    deneme_isim = input("Deneme'nin ismi: ")
    deneme_not = input("Notlarınız: ")
    username = os.getlogin()
    try:
        deneme_file = open(f"C:\\Users\\{username}\\Desktop\\Denemeler.txt","a")
        deneme_file.write("Deneme ismi: {}  Türkçe neti: {}     Matematik neti: {}     Sosyal neti: {}     Fen neti: {}".format(deneme_isim,self.turk,self.math,self.social,self.scnc)+"\n"+deneme_not+"\n")
    except FileExistsError:
        deneme_file = open(f"C:\\Users\\{username}\\Desktop\\Denemeler.txt","w")
        deneme_file.write("Deneme ismi: {}  Türkçe neti: {}     Matematik neti: {}     Sosyal neti: {}     Fen neti: {}".format(deneme_isim,self.turk,self.math,self.social,self.scnc)+"\n"+deneme_not+"\n")
while 1:
    secenek = input("Yeni/Çıkış?\n").title()
    if secenek == "Yeni":
        deneme_kayit = deneme(int(input("Türkçe: ")),int(input("Matematik: ")),int(input("Sosyal: ")),int(input("Fen: ")))
        deneme_kayit.kontrol()
        if a == True:
            yazdir(deneme_kayit)
        else:
            break
    elif secenek == "Çıkış":
        break
    else:
        print("Böyle bir seçenek bulunmamaktadır.")
        continue
        
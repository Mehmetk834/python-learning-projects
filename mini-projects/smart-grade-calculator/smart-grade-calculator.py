dersler = []
notlar = []

ders_sayisi = int(input("Kaç ders gireceksiniz: "))

for i in range(ders_sayisi):
    ders_adi = input(f"{i+1}. dersin adı: ")

    not_degeri = int(input("Notunuzu giriniz (0-100): "))
    while not_degeri < 0 or not_degeri > 100:
        print("Yanlış not girdiniz! 0-100 arası girin.")
        not_degeri = int(input("Notunuzu giriniz (0-100): "))

    dersler.append(ders_adi)
    notlar.append(not_degeri)

toplam = sum(notlar)
ortalama = toplam / ders_sayisi

print("Ortalama:", ortalama)

if 90 <= ortalama <= 100:
    harf = "AA"
elif 85 <= ortalama <= 89:
    harf = "BA"
elif 80 <= ortalama <= 84:
    harf = "BB"
elif 75 <= ortalama <= 79:
    harf = "CB"
elif 70 <= ortalama <= 74:
    harf = "CC"
elif 65 <= ortalama <= 69:
    harf = "DC"
elif 60 <= ortalama <= 64:
    harf = "DD"
elif 50 <= ortalama <= 59:
    harf = "FD"
else:
    harf = "FF"

print("Harf Notu:", harf)
print("Durum:", "Geçti" if ortalama >= 50 else "Kaldı")


def en_yuksek_not_bul(dersler, notlar):
    en_yuksek = max(notlar)
    index = notlar.index(en_yuksek)
    print(f"En yüksek notunuz {dersler[index]} dersinden aldığınız {en_yuksek}'dir.")


def en_dusuk_not_bul(dersler, notlar):
    en_dusuk = min(notlar)
    index = notlar.index(en_dusuk)
    print(f"En düşük notunuz {dersler[index]} dersinden aldığınız {en_dusuk}'dir.")


en_yuksek_not_bul(dersler, notlar)
en_dusuk_not_bul(dersler, notlar)
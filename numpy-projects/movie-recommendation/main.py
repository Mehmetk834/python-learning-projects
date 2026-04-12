
import numpy as np

filmler = ["Titanic", "Matrix", "Interstellar", "Batman", "Avatar"]

puanlar = np.array([
    [5,4,0,0,3],
    [5,0,4,0,0],
    [0,4,5,3,0],
    [0,0,4,5,4]
])

kullanicilar = ["Kullanıcı 1", "Kullanıcı 2", "Kullanıcı 3", "Kullanıcı 4"]

kullanici_adlari = ["kullanici1", "kullanici2", "kullanici3", "kullanici4"]
sifreler = ["123", "456", "789", "abc"]

print("=== Film Öneri Sistemine Hoş Geldiniz ===\n")

kullanici_adi_giris = input("Kullanıcı adınızı girin: ")
sifre_giris = input("Şifrenizi girin: ")

if kullanici_adi_giris in kullanici_adlari:

    kullanici_index = kullanici_adlari.index(kullanici_adi_giris)

    if sifreler[kullanici_index] == sifre_giris:
        print("\nGiriş başarılı!\n")
        hedef_kullanici_index = kullanici_index
        hedef_kullanici = puanlar[hedef_kullanici_index]

    else:
        print("Şifre yanlış!")
        exit()

else:
    print("Kullanıcı bulunamadı!")
    exit()


def kosinus_benzerligi(a, b):

    skaler_carpim = np.dot(a, b)

    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)

    benzerlik = skaler_carpim / (norm_a * norm_b)

    return benzerlik


benzerlikler = []

for kullanici in puanlar:
    sonuc = kosinus_benzerligi(hedef_kullanici, kullanici)
    benzerlikler.append(sonuc)

benzerlikler = np.array(benzerlikler)

benzerlikler[hedef_kullanici_index] = 0

en_benzer_kullanici = np.argmax(benzerlikler)


onerilen_filmler = []

for i in range(len(filmler)):
    if hedef_kullanici[i] == 0 and puanlar[en_benzer_kullanici][i] > 0:
        onerilen_filmler.append(filmler[i])


print("Size en çok benzeyen kullanıcı:", kullanicilar[en_benzer_kullanici])

print("\nÖnerilen filmler:")

if len(onerilen_filmler) == 0:
    print("Size önerilecek yeni film bulunamadı.")
else:
    for film in onerilen_filmler:
        print("-", film)

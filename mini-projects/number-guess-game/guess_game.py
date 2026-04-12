import random

tutulan_sayi = random.randint(1, 100)
kalan_hak = 4
puan = 100
deneme_sayisi = 0

print("1 ile 100 arasında bir sayı tahmin et")
print(f"Başlangıç puanın: {puan}")

while kalan_hak > 0:
    try:
        tahmin = int(input("Tahminin: "))
    except ValueError:
        print("Lütfen sadece sayı gir")
        continue

    if tahmin < 1 or tahmin > 100:
        print("1 ile 100 arasında bir sayı gir")
        continue

    deneme_sayisi += 1

    if tahmin == tutulan_sayi:
        print(f"Tebrikler! {deneme_sayisi}. denemede bildin 🎉")
        print(f"Puanın: {puan}")
        break

    kalan_hak -= 1
    puan -= 25

    if kalan_hak == 0:
        print("Hakkın bitti")
        print(f"Doğru sayı: {tutulan_sayi}")
        print(f"Puanın: {puan}")
        break

    if tahmin < tutulan_sayi:
        print("Daha büyük bir sayı gir")
    else:
        print("Daha küçük bir sayı gir")

    print(f"Kalan hak: {kalan_hak}")
    print(f"Kalan puan: {puan}")


bakiye = 0
dogru_kullanici_adi = "Mehmet"
dogru_sifre = 12345
giris_hakki = 3
islem_gecmisi = []


while giris_hakki > 0:
    girilen_kullanici_adi = input("Kullanıcı adınızı giriniz: ")

    try:
        girilen_sifre = int(input("Şifrenizi giriniz: "))
    except ValueError:
        print("Şifre sadece sayı olmalıdır.")
        continue

    if girilen_kullanici_adi == dogru_kullanici_adi and girilen_sifre == dogru_sifre:
        print("Giriş başarılı.")

        while True:
            print("\n--- ATM MENÜ ---")
            print("1 - Bakiye Görüntüle")
            print("2 - Para Yatır")
            print("3 - Para Çek")
            print("4 - İşlem Geçmişi")
            print("5 - Çıkış")

            secim = input("Seçiminiz: ")

            if secim == "1":
                print("Mevcut bakiyeniz:", bakiye)

            elif secim == "2":
                try:
                    yatirilan_miktar = int(input("Yatırmak istediğiniz tutar: "))
                    if yatirilan_miktar > 0:
                        bakiye += yatirilan_miktar
                        islem_gecmisi.append(f"{yatirilan_miktar} TL yatırıldı")
                        print("Para yatırıldı. Güncel bakiyeniz:", bakiye)
                    else:
                        print("Miktar 0'dan büyük olmalıdır.")
                except ValueError:
                    print("Lütfen sadece sayı giriniz.")

            elif secim == "3":
                try:
                    cekilen_miktar = int(input("Çekmek istediğiniz tutar: "))
                    if cekilen_miktar > 0 and cekilen_miktar <= bakiye:
                        bakiye -= cekilen_miktar
                        islem_gecmisi.append(f"{cekilen_miktar} TL çekildi")
                        print("Para çekildi. Güncel bakiyeniz:", bakiye)
                    else:
                        print("Yetersiz bakiye veya geçersiz miktar.")
                except ValueError:
                    print("Lütfen sadece sayı giriniz.")

            elif secim == "4":
                if len(islem_gecmisi) == 0:
                    print("Henüz işlem yapılmadı.")
                else:
                    print("\nİşlem Geçmişi:")
                    for islem in islem_gecmisi:
                        print("-", islem)

            elif secim == "5":
                print("Çıkış yapılıyor.")
                break

            else:
                print("Geçersiz seçim.")

        break

    else:
        giris_hakki -= 1
        print("Kullanıcı adı veya şifre yanlış.")
        print("Kalan hakkınız:", giris_hakki)

        if giris_hakki == 0:
            print("Hesabınız bloke edildi.")
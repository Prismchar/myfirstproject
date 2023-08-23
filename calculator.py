while True:
    deger = float(input("deger giriniz:"))
    ikincideger = float(input("deger giriniz:"))
    toplam = deger + ikincideger
    print(toplam)
    sonuc = input("baska bir islem yapmak ister misiniz?")
    if sonuc == "hayir":
        break
else:
    print("cikis")

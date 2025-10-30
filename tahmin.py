import random

print("🎲 Tahmin Etme Oyununa Hoş Geldin!")
print("1 ile 100 arasında bir sayı tuttum. Bakalım tahmin edebilecek misin?")

# Bilgisayarın tuttuğu rastgele sayı
sayi = random.randint(1, 100)

tahmin_sayisi = 0

while True:
    tahmin = input("Tahminini gir (veya çıkmak için 'q' yaz): ")

    if tahmin.lower() == 'q':
        print("Oyundan çıkılıyor. Görüşürüz!")
        break

    if not tahmin.isdigit():
        print("Lütfen sadece sayı gir.")
        continue

    tahmin = int(tahmin)
    tahmin_sayisi += 1

    if tahmin < sayi:
        print("Daha büyük bir sayı dene 🔼")
    elif tahmin > sayi:
        print("Daha küçük bir sayı dene 🔽")
    else:
        print(f"🎉 Tebrikler! {tahmin_sayisi} denemede doğru tahmin ettin.")
        break

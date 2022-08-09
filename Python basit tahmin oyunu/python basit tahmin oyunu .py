import random
sayi= random.randint(1,10)
can = int(input('kaç hak kullanmak istersiniz:'))
hak = can
sayac = 0

while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input('1 ile 10 arasında bir tahmin giriniz:'))
    if (sayi == tahmin):
        print(f'Tebrikler {sayac} defada bildiniz. Toplam puanınız: {100-(100/can) * (sayac -1)}')
        break
    elif (sayi > tahmin):
        print('Daha büyük bir sayı giriniz:')
    else:
        print('Daha küçük bir sayı giriniz:')
        if (hak ==  0):
            print(f'Hakkınız bitmiştir. Tutulan sayı: {sayi}')
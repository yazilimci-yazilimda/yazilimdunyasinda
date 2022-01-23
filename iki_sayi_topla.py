gui="""
1- Topla
2- Çıkar
3- Çarp
4- Böl

"""

islem = input("Hangi işlem yapılacak: ")

if islem not in [1,2,3,4]:
	input("Çıkılıyor...")
	quit()

sayi1 = int(input("Sayı 1: "))
sayi2 = int(input("Sayı 2: "))

if islem == 1:
	sonuc = sayi1 + sayi2
elif islem == 2:
	sonuc = sayi1 - sayi2
if islem == 3:
	sonuc = sayi1 * sayi2
if islem == 4:
	sonuc = sayi1 / sayi2
	
print("Sonuç = " + sonuc)
	
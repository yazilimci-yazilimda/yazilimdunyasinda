kac = int(input("Kaça kadar yazılacak: "))
arasayi = 1
ilksayi = 1
sonsayi = 1
sonuc = []
sonuc.append(ilksayi)
for i in range(1, kac):
	sonuc.append(sonsayi)
	arasayi = sonsayi
	sonsayi += ilksayi
	ilksayi = arasayi
	
print(sonuc)
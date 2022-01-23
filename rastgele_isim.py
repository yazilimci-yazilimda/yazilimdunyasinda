import random

isimler = ["Osman", "Ali", "Kemal", "Fatma", "Ayşe", "Ekrem", "Sümeyra", "Kübra"]

soyisimler = ["Gökmen", "Durğun", "Yılmaz", "Kahraman"]

while True:
	isim_id = random.randint(0,len(isimler)+1)
	soyisim_id = random.randint(0,len(soyisimler)+1)
	
	isim = isimler[isim_id]
	soyisim = soyisimler[soyisim_id]
	
	print("Rastgele isim ---> ", (isim + soyisim), end="\n\n\n")
	
	devam = input("Yeni isim üretilsin mi?\n")
	if devam == "evet":
		continue
	else:
		break

sayı = int(input("sayı giriniz :"))

liste = []

for i in range(1,sayı ):

    if  sayı % i == 0:
        liste.append(i)

toplam = 0
for i in liste:
    toplam +=i

if sayı == toplam :
    print("sayı mukemmeldir")
else:
    print("mükemmel sayı değildir")

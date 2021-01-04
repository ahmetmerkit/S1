print("             ATM UYGULAMASI              ")
print("""
1-Bakiye Durumu öğrenmek içib 1 e basın 
2-Bakiye eklemek için 2 ye basın 
3-Bakiye çekmek için 3 e basın
çıkış yapmak için ' q '

""")
bakiye = 50

while True :
    sorgu = input("İşlem seçin")
    if sorgu == 'q':
        print("başarıyla çıkıldı")
        break
    elif sorgu == '1':
        print("bakiye durumunuz ...:",bakiye)
    elif sorgu == '2':
        tutar = int(input("eklemek istediğiniz bakıyei girin"))
        bakiye += tutar
        print("bakiyeniz güncellendi : ",bakiye)
    elif sorgu =='3':
        tutar2= int(input("çekmek istediğiniz bakıyei girin"))
        bakiye = bakiye - tutar2
        print("bakiyeniz güncellendi : ", bakiye)
    else:
        print("hatalı giriş")

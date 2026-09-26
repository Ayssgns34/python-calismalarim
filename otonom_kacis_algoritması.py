import random
import time
while True:
    on_mesafe=random.randint(10,100)
    sag_mesafe=random.randint(10,100)
    sol_mesafe=random.randint(10,100)
    print(f"sensörler -> Ön:{on_mesafe}cm |Sağ:{sag_mesafe}cm |Sol: {sol_mesafe}cm")

    if on_mesafe >40 :
        print("Durum: Ön taraf temiz,ileri gidiliyor")
    else:
        print("Dikkat ! önde engel var yeni yön aranıyor...")

        if sag_mesafe>sol_mesafe :
            print("Karar :Sağ taraf daha güvenli, SAĞA dönülüyor")
        elif sag_mesafe<sol_mesafe :
            print("Karar:Sol daha güvenli,SOLA dönülüyor")
        else:
            print("Karar:İki tarafta eşit,mecburi SAĞA dönülüyor.")
        if sag_mesafe<40 and sol_mesafe<40:
            print("KRİTİK DURUM: Çıkmaz sokak! Araç GERİ gidiyor")
        if sag_mesafe>sol_mesafe :
            print("Karar :Sağ taraf daha güvenli, SAĞA dönülüyor")
        elif sag_mesafe<sol_mesafe :
            print("Karar:Sol daha güvenli,SOLA dönülüyor")
        else:
            print("Karar:İki tarafta eşit,mecburi SAĞA dönülüyor.")
        time.sleep(1)
        print("-"*40)
        

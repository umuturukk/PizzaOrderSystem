from datetime import datetime
import time
import Pizza

def main():
    def odeme():
        print("Ödemeye geçiliyor..\n")
        time.sleep(1)
        ad = input("Adinizi giriniz: ")
        tcNo = input("Kimlik numaranizi giriniz: ")
        krediKartNo = input("Kart numaranizi giriniz: ")
        krediKartSifre = input("Kart şifrenizi giriniz: ")

        with open("odeme.txt", "a", encoding = "utf-8") as odeme:
            odeme.write("\n" + ad + ", " + tcNo + ", " + krediKartNo + ", " + krediKartSifre + ", " + str(datetime.now().date()))
            odeme.close()

        print("Ödeme işlemi başarıyla tamamlandı. Siparişiniz en kısa sürede ulaştırılacaktır.")

    while True:
        secim = input("Yapmak işlediğiniz işlemi seçiniz: ")
        if secim == "1":
            with open("menu.txt", "r", encoding = "utf-8") as menu:
                contents = menu.read()
                print(contents)

            pizzaSecimi = input("Menüye göz gezdirip sipariş etmek istediğiniz pizzaya karşılık gelen numarayı tuşlayınız: ")
            if pizzaSecimi == "1":
                margherita = Pizza.Margherita()
                bill = margherita.price
                print("Margherita pizza seçiminde bulundunuz.")
                margherita.get_description()

                exMalzeme = input("Pizzanıza ek olarak eklemek istediğiniz malzemeyi tuşlayınız (istemiyorsanız 'h'): ")
                if exMalzeme == "h":
                    print(f'Sos istemediniz. Pizzanızın son fiyatı {bill} ₺.')
                    odeme()
                    break
                elif exMalzeme == "11":
                    bill += 3
                    print(f'Pizzanıza ekstra malzeme olarak zeytin eklenecektir. Pizzanızın son fiyatı {bill} ₺.')
                    odeme()
                    break
                elif exMalzeme == "12":
                    bill += 5
                    print(f'Pizzanıza ekstra malzeme olarak çeşitli mantarlar eklenecektir. Pizzanızın son fiyatı {bill} ₺.')
                    odeme()
                    break
                elif exMalzeme == "13":
                    bill += 7
                    print(f'Pizzanıza ekstra malzeme olarak keçi peyniri eklenecektir. Pizzanızın son fiyatı {bill} ₺.')
                    odeme()
                    break
                elif exMalzeme == "14":
                    bill += 10
                    print(f'Pizzanıza ekstra malzeme olarak et eklenecektir. Pizzanızın son fiyatı {bill} ₺.')
                    odeme()
                    break
                elif exMalzeme == "15":
                    bill += 3
                    print(f'Pizzanıza ekstra malzeme olarak soğan eklenecektir. Pizzanızın son fiyatı {bill} ₺.')
                    odeme()
                    break
                elif exMalzeme == "16":
                    bill += 5
                    print(f'Pizzanıza ekstra malzeme olarak mısır eklenecektir. Pizzanızın son fiyatı {bill} ₺.')
                    odeme()
                    break

            elif pizzaSecimi == "2":
                pepperoni = Pizza.Pepperoni()
                bill = pepperoni.price
                print("Pepperoni pizza seçiminde bulundunuz.")
                pepperoni.get_description()

                exMalzeme = input("Pizzanıza ek olarak eklemek istediğiniz malzemeyi tuşlayınız (istemiyorsanız 'h'): ")
                if exMalzeme == "h":
                    print(f'Sos istemediniz. Pizzanızın son fiyatı {bill} ₺.')
                    odeme()
                    break
                elif exMalzeme == "11":
                    bill += 3
                    print(f'Pizzanıza ekstra malzeme olarak zeytin eklenecektir. Pizzanızın son fiyatı {bill} ₺.')
                    odeme()
                    break
                elif exMalzeme == "12":
                    bill += 5
                    print(f'Pizzanıza ekstra malzeme olarak çeşitli mantarlar eklenecektir. Pizzanızın son fiyatı {bill} ₺.')
                    odeme()
                    break
                elif exMalzeme == "13":
                    bill += 7
                    print(f'Pizzanıza ekstra malzeme olarak keçi peyniri eklenecektir. Pizzanızın son fiyatı {bill} ₺.')
                    odeme()
                    break
                elif exMalzeme == "14":
                    bill += 10
                    print(f'Pizzanıza ekstra malzeme olarak et eklenecektir. Pizzanızın son fiyatı {bill} ₺.')
                    odeme()
                    break
                elif exMalzeme == "15":
                    bill += 3
                    print(f'Pizzanıza ekstra malzeme olarak soğan eklenecektir. Pizzanızın son fiyatı {bill} ₺.')
                    odeme()
                    break
                elif exMalzeme == "16":
                    bill += 5
                    print(f'Pizzanıza ekstra malzeme olarak mısır eklenecektir. Pizzanızın son fiyatı {bill} ₺.')
                    odeme()
                    break

            elif pizzaSecimi == "3":
                fourCheese = Pizza.FourCheese()
                bill = fourCheese.price
                print("Dört peynirli pizza seçiminde bulundunuz.")
                fourCheese.get_description()

                exMalzeme = input("Pizzanıza ek olarak eklemek istediğiniz malzemeyi tuşlayınız (istemiyorsanız 'h'): ")
                if exMalzeme == "h":
                    print(f'Sos istemediniz. Pizzanızın son fiyatı {bill} ₺.')
                    odeme()
                    break
                elif exMalzeme == "11":
                    bill += 3
                    print(f'Pizzanıza ekstra malzeme olarak zeytin eklenecektir. Pizzanızın son fiyatı {bill} ₺.')
                    odeme()
                    break
                elif exMalzeme == "12":
                    bill += 5
                    print(f'Pizzanıza ekstra malzeme olarak çeşitli mantarlar eklenecektir. Pizzanızın son fiyatı {bill} ₺.')
                    odeme()
                    break
                elif exMalzeme == "13":
                    bill += 7
                    print(f'Pizzanıza ekstra malzeme olarak keçi peyniri eklenecektir. Pizzanızın son fiyatı {bill} ₺.')
                    odeme()
                    break
                elif exMalzeme == "14":
                    bill += 10
                    print(f'Pizzanıza ekstra malzeme olarak et eklenecektir. Pizzanızın son fiyatı {bill} ₺.')
                    odeme()
                    break
                elif exMalzeme == "15":
                    bill += 3
                    print(f'Pizzanıza ekstra malzeme olarak soğan eklenecektir. Pizzanızın son fiyatı {bill} ₺.')
                    odeme()
                    break
                elif exMalzeme == "16":
                    bill += 5
                    print(f'Pizzanıza ekstra malzeme olarak mısır eklenecektir. Pizzanızın son fiyatı {bill} ₺.')
                    odeme()
                    break

            elif pizzaSecimi == "4":
                bbqChicken = Pizza.BbqChicken()
                bill = bbqChicken.price
                print("Tavuklu barbekülü pizza seçiminde bulundunuz.")
                bbqChicken.get_description()

                exMalzeme = input("Pizzanıza ek olarak eklemek istediğiniz malzemeyi tuşlayınız (istemiyorsanız 'h'): ")
                if exMalzeme == "h":
                    print(f'Sos istemediniz. Pizzanızın son fiyatı {bill} ₺.')
                    odeme()
                    break
                elif exMalzeme == "11":
                    bill += 3
                    print(f'Pizzanıza ekstra malzeme olarak zeytin eklenecektir. Pizzanızın son fiyatı {bill} ₺.')
                    odeme()
                    break
                elif exMalzeme == "12":
                    bill += 5
                    print(f'Pizzanıza ekstra malzeme olarak çeşitli mantarlar eklenecektir. Pizzanızın son fiyatı {bill} ₺.')
                    odeme()
                    break
                elif exMalzeme == "13":
                    bill += 7
                    print(f'Pizzanıza ekstra malzeme olarak keçi peyniri eklenecektir. Pizzanızın son fiyatı {bill} ₺.')
                    odeme()
                    break
                elif exMalzeme == "14":
                    bill += 10
                    print(f'Pizzanıza ekstra malzeme olarak et eklenecektir. Pizzanızın son fiyatı {bill} ₺.')
                    odeme()
                    break
                elif exMalzeme == "15":
                    bill += 3
                    print(f'Pizzanıza ekstra malzeme olarak soğan eklenecektir. Pizzanızın son fiyatı {bill} ₺.')
                    odeme()
                    break
                elif exMalzeme == "16":
                    bill += 5
                    print(f'Pizzanıza ekstra malzeme olarak mısır eklenecektir. Pizzanızın son fiyatı {bill} ₺.')
                    odeme()
                    break
            else:
                print("Henüz 4 adet pizza çeşidimiz bulunmaktadır. Menüye göz gezdirip istediğiniz pizzaya karşılık gelen numarayı tuşlayınız.(1-4)")
                
        elif secim == "0":
            print("Sistemden çıkış yapılıyor...")
            break

        else:
            print("Lütfen 0 veya 1 seçeneklerinden birini tuşlayınız.")
            continue

if __name__ == "__main__":
    main()
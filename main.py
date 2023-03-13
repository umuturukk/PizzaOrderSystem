from datetime import datetime
import time
from pizza import Pizza
import csv

def main():
    def odeme():
        print("Ödemeye geçiliyor..\n")
        time.sleep(1)
        ad = input("Adinizi giriniz: ")
        tcNo = input("Kimlik numaranizi giriniz: ")
        krediKartNo = input("Kart numaranizi giriniz: ")
        krediKartSifre = input("Kart şifrenizi giriniz: ")

        veriler = [[ad, tcNo, krediKartNo, krediKartSifre, datetime.now().date()]]

        with open("orders_database.csv", "a", newline = '') as odeme:
            odeme2 = csv.writer(odeme)
            odeme2.writerows(veriler)

        print("Ödeme işlemi başariyla tamamlandi. Siparişiniz en kisa sürede ulaştirilacaktir.")

    while True:
        secim = input("Menüyü görüntülemek için 1'i sistemden çikmak için 0'i tuşlayiniz: ")
        if secim == "1":
            with open("menu.txt", "r", encoding = "utf-8") as menu:
                contents = menu.read()
                print(contents)

            pizzaSecimi = input("Menüye göz gezdirip sipariş etmek istediğiniz pizzaya karşilik gelen numarayi tuşlayiniz: ")
            if pizzaSecimi == "1":
                margherita = Pizza.Margherita()
                bill = margherita.price
                print("Margherita pizza seçiminde bulundunuz.")
                margherita.get_description()

                exMalzeme = input("Pizzaniza ek olarak eklemek istediğiniz malzemeyi tuşlayiniz (istemiyorsaniz 'h'): ")
                if exMalzeme == "h":
                    print(f'Sos istemediniz. Pizzanizin son fiyati {bill} ₺.')
                    odeme()
                    break
                elif exMalzeme == "11":
                    bill += 3
                    print(f'Pizzaniza ekstra malzeme olarak zeytin eklenecektir. Pizzanizin son fiyati {bill} ₺.')
                    odeme()
                    break
                elif exMalzeme == "12":
                    bill += 5
                    print(f'Pizzaniza ekstra malzeme olarak çeşitli mantarlar eklenecektir. Pizzanizin son fiyati {bill} ₺.')
                    odeme()
                    break
                elif exMalzeme == "13":
                    bill += 7
                    print(f'Pizzaniza ekstra malzeme olarak keçi peyniri eklenecektir. Pizzanizin son fiyati {bill} ₺.')
                    odeme()
                    break
                elif exMalzeme == "14":
                    bill += 10
                    print(f'Pizzaniza ekstra malzeme olarak et eklenecektir. Pizzanizin son fiyati {bill} ₺.')
                    odeme()
                    break
                elif exMalzeme == "15":
                    bill += 3
                    print(f'Pizzaniza ekstra malzeme olarak soğan eklenecektir. Pizzanizin son fiyati {bill} ₺.')
                    odeme()
                    break
                elif exMalzeme == "16":
                    bill += 5
                    print(f'Pizzaniza ekstra malzeme olarak misir eklenecektir. Pizzanizin son fiyati {bill} ₺.')
                    odeme()
                    break

            elif pizzaSecimi == "2":
                pepperoni = Pizza.Pepperoni()
                bill = pepperoni.price
                print("Pepperoni pizza seçiminde bulundunuz.")
                pepperoni.get_description()

                exMalzeme = input("Pizzaniza ek olarak eklemek istediğiniz malzemeyi tuşlayiniz (istemiyorsaniz 'h'): ")
                if exMalzeme == "h":
                    print(f'Sos istemediniz. Pizzanizin son fiyati {bill} ₺.')
                    odeme()
                    break
                elif exMalzeme == "11":
                    bill += 3
                    print(f'Pizzaniza ekstra malzeme olarak zeytin eklenecektir. Pizzanizin son fiyati {bill} ₺.')
                    odeme()
                    break
                elif exMalzeme == "12":
                    bill += 5
                    print(f'Pizzaniza ekstra malzeme olarak çeşitli mantarlar eklenecektir. Pizzanizin son fiyati {bill} ₺.')
                    odeme()
                    break
                elif exMalzeme == "13":
                    bill += 7
                    print(f'Pizzaniza ekstra malzeme olarak keçi peyniri eklenecektir. Pizzanizin son fiyati {bill} ₺.')
                    odeme()
                    break
                elif exMalzeme == "14":
                    bill += 10
                    print(f'Pizzaniza ekstra malzeme olarak et eklenecektir. Pizzanizin son fiyati {bill} ₺.')
                    odeme()
                    break
                elif exMalzeme == "15":
                    bill += 3
                    print(f'Pizzaniza ekstra malzeme olarak soğan eklenecektir. Pizzanizin son fiyati {bill} ₺.')
                    odeme()
                    break
                elif exMalzeme == "16":
                    bill += 5
                    print(f'Pizzaniza ekstra malzeme olarak misir eklenecektir. Pizzanizin son fiyati {bill} ₺.')
                    odeme()
                    break

            elif pizzaSecimi == "3":
                fourCheese = Pizza.FourCheese()
                bill = fourCheese.price
                print("Dört peynirli pizza seçiminde bulundunuz.")
                fourCheese.get_description()

                exMalzeme = input("Pizzaniza ek olarak eklemek istediğiniz malzemeyi tuşlayiniz (istemiyorsaniz 'h'): ")
                if exMalzeme == "h":
                    print(f'Sos istemediniz. Pizzanizin son fiyati {bill} ₺.')
                    odeme()
                    break
                elif exMalzeme == "11":
                    bill += 3
                    print(f'Pizzaniza ekstra malzeme olarak zeytin eklenecektir. Pizzanizin son fiyati {bill} ₺.')
                    odeme()
                    break
                elif exMalzeme == "12":
                    bill += 5
                    print(f'Pizzaniza ekstra malzeme olarak çeşitli mantarlar eklenecektir. Pizzanizin son fiyati {bill} ₺.')
                    odeme()
                    break
                elif exMalzeme == "13":
                    bill += 7
                    print(f'Pizzaniza ekstra malzeme olarak keçi peyniri eklenecektir. Pizzanizin son fiyati {bill} ₺.')
                    odeme()
                    break
                elif exMalzeme == "14":
                    bill += 10
                    print(f'Pizzaniza ekstra malzeme olarak et eklenecektir. Pizzanizin son fiyati {bill} ₺.')
                    odeme()
                    break
                elif exMalzeme == "15":
                    bill += 3
                    print(f'Pizzaniza ekstra malzeme olarak soğan eklenecektir. Pizzanizin son fiyati {bill} ₺.')
                    odeme()
                    break
                elif exMalzeme == "16":
                    bill += 5
                    print(f'Pizzaniza ekstra malzeme olarak misir eklenecektir. Pizzanizin son fiyati {bill} ₺.')
                    odeme()
                    break

            elif pizzaSecimi == "4":
                bbqChicken = Pizza.BbqChicken()
                bill = bbqChicken.price
                print("Tavuklu barbekülü pizza seçiminde bulundunuz.")
                bbqChicken.get_description()

                exMalzeme = input("Pizzaniza ek olarak eklemek istediğiniz malzemeyi tuşlayiniz (istemiyorsaniz 'h'): ")
                if exMalzeme == "h":
                    print(f'Sos istemediniz. Pizzanizin son fiyati {bill} ₺.')
                    odeme()
                    break
                elif exMalzeme == "11":
                    bill += 3
                    print(f'Pizzaniza ekstra malzeme olarak zeytin eklenecektir. Pizzanizin son fiyati {bill} ₺.')
                    odeme()
                    break
                elif exMalzeme == "12":
                    bill += 5
                    print(f'Pizzaniza ekstra malzeme olarak çeşitli mantarlar eklenecektir. Pizzanizin son fiyati {bill} ₺.')
                    odeme()
                    break
                elif exMalzeme == "13":
                    bill += 7
                    print(f'Pizzaniza ekstra malzeme olarak keçi peyniri eklenecektir. Pizzanizin son fiyati {bill} ₺.')
                    odeme()
                    break
                elif exMalzeme == "14":
                    bill += 10
                    print(f'Pizzaniza ekstra malzeme olarak et eklenecektir. Pizzanizin son fiyati {bill} ₺.')
                    odeme()
                    break
                elif exMalzeme == "15":
                    bill += 3
                    print(f'Pizzaniza ekstra malzeme olarak soğan eklenecektir. Pizzanizin son fiyati {bill} ₺.')
                    odeme()
                    break
                elif exMalzeme == "16":
                    bill += 5
                    print(f'Pizzaniza ekstra malzeme olarak misir eklenecektir. Pizzanizin son fiyati {bill} ₺.')
                    odeme()
                    break
            else:
                print("Henüz 4 adet pizza çeşidimiz bulunmaktadir. Menüye göz gezdirip istediğiniz pizzaya karşilik gelen numarayi tuşlayiniz.(1-4)")
                
        elif secim == "0":
            print("Sistemden çikiş yapiliyor...")
            break

        else:
            print("Lütfen 0 veya 1 seçeneklerinden birini tuşlayiniz.")
            continue

if __name__ == "__main__":
    main()
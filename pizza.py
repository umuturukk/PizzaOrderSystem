class Pizza:
    def __init__(self):
        self.margherita = self.Margherita()
        self.pepperoni = self.Pepperoni()
        self.fourcheese = self.FourCheese()
        self.bbqchicken = self.BbqChicken()
    
    def get_cost(self):
        print(f"{self.name}'in fiyati {self.price} ₺'dir.")
    
    def get_description(self):
        print(self.description)
    
    class Margherita():
        def __init__(self):
            self.name = "Margherita"
            self.price = 15
            self.description = "Margarita pizza, domates, mozarella, fesleğen, zeytinyaği ve tuzla yapilan Napoli pizzasidir."
    
        def get_cost(self):
            super().get_cost()
            
        def get_description(self):
            print(self.description)
            
    class Pepperoni():
        def __init__(self):
            self.name = "Pepperoni"
            self.price = 25
            self.description = "Pepperoni pizza, pepperoni, pepperoni sos, mozerella peyniri, misir, yeşil zeytin ve siyah zeytin içerir."
        
        def get_cost(self):
            super().get_cost()
            
        def get_description(self):
            print(self.description)
            
    class FourCheese():
        def __init__(self):
            self.name = "Dört Peynirli Pizza"
            self.price = 20
            self.description = "Dört peynirli pizza, İtalyan mutfağindan bir pizza çeşididir. Dört peynir birlikte eritilir ve domates sosu olmadan pizza hamurunun üzerine konur."
        
        def get_cost(self):
            super().get_cost()
        
        def get_description(self):
            print(self.description)
            
    class BbqChicken():
        def __init__(self):
            self.name = "Tavuklu Barbekü soslu Pizza"
            self.price = 25
            self.description = "İçeriğinde tavuk, barbekü sos, misir, soğan, kapya biber ve az miktarda peynir bulunur."
    
        def get_cost(self):
            super().get_cost()
        
        def get_description(self):
            print(self.description)
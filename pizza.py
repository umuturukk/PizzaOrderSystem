class Pizza:
    def __init__(self):
        self.margherita = Margherita()
        self.pepperoni = Pepperoni()
        self.fourcheese = FourCheese()
        self.bbqchicken = BbqChicken()
    
    def get_cost(self):
        print(f"{self.name}'in fiyatı {self.price} ₺'dir.")
    
    def get_description(self):
        print(self.description)
    
    class Margherita(Pizza):
        def __init__(self):
            self.name = "Margherita"
            self.price = 15
            self.description = "Margarita pizza, domates, mozarella, fesleğen, zeytinyağı ve tuzla yapılan Napoli pizzasıdır."
    
        def get_cost(self):
            super().get_cost()
            
        def get_description(self):
            super().get_description()
            
    class Pepperoni(Pizza):
        def __init__(self):
            self.name = "Pepperoni"
            self.price = 25
            self.description = "Pepperoni pizza, pepperoni, pepperoni sos, mozerella peyniri, mısır, yeşil zeytin ve siyah zeytin içerir."
        
        def get_cost(self):
            super().get_cost()
            
        def get_description(self):
            super().get_description()
            
    class FourCheese(Pizza):
        def __init__(self):
            self.name = "Dört Peynirli Pizza"
            self.price = 20
            self.description = "Dört peynirli pizza, İtalyan mutfağından bir pizza çeşididir. Dört peynir birlikte eritilir ve domates sosu olmadan pizza hamurunun üzerine konur."
        
        def get_cost(self):
            super().get_cost()
        
        def get_description(self):
            super().get_description()
            
    class BbqChicken(Pizza):
        def __init__(self):
            self.name = "Tavuklu Barbekü soslu Pizza"
            self.price = 25
            self.description = "İçeriğinde tavuk, barbekü sos, mısır, soğan, kapya biber ve az miktarda peynir bulunur."
    
        def get_cost(self):
            super().get_cost()
        
        def get_description(self):
            super().get_description()
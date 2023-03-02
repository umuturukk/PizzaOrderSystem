class Pizza:
    def __init__(self, pizzaName, pizzaSauce, pizzaCost):
        self.__pizzaName = pizzaName
        self.__pizzaSauce = pizzaSauce
        self.__pizzaCost = pizzaCost
        
    def get_description(self):
        print(f'Seçmiş olduğunuz pizza : {self.__pizzaName}\nPizzaya ek olarak seçmiş olduğunuz sos : {self.__pizzaSauce}')

    def get_cost(self):
        print(f'Seçmiş olduğunuz pizza tabani ve sos ile birlikte pizzanizin maliyeti {self.__pizzaCost} ₺.')
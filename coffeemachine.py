
class Product:
    def __init__(self, name, price, recipe):
        self.name = name
        self.price = price
        self.recipe = recipe

    def get_prices(self):
        return self.price

    def make(self):
        print(self.recipe)


class CashBox:
    def __init__(self):
        pass

class Selector:
    def __init__(self, cashbox):
        self.cashBox = cashbox
        self.products = []
        self.products.append(Product("Black" 35, "add cup, poor coffe"))

class CoffeeMachine:
    def __init__(self):
        sefl.cashBox = cashBox()
        self.selector = Selector(self.cashBox)

    def one_action(self):
        #Menu
        pass


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
        self.credit = 0
        self.total_cash = 0
        

    def deposit(self, amount):
        if amount not in(5,10,25,50):
            print("INVALID AMOUNT")
            print("We only take half-dollars, quarters, dimes, and nickels.")
            return
        self.credit += amount
        print("Depositing " +str(amount)+" cents. You Have " +str(self.credit) +" cents credit.")

    def return_coins(self):
        print("Returning " +str(self.credit)+ " cents.")
        self.credit = 0
        
      
    
    def have_you(self, amount):
        return amount <= self.credit

    def deduct(self, amount):
        if self.have_you(amount):
            self.credit -= amount
            self.total_cash+= amount
            if self.credit > 0:
                print("Returning " + str(self.credit) + " cents.")
                self.credit = 0
        

    def total(self):
        return self.total_cash
        

        

class Selector:
    def __init__(self, cashbox, products):
        self.cashBox = cashbox
        self.products = products
        

    def select(self, choiceIndex):
        if choiceIndex <  1 or choiceIndex > 5:
            print("Invalid Choice")
            return
        choice = self.products[choiceIndex - 1]
        if not self.cashBox.have_you(choice.get_prices()):
            print("Sorry. Not enough money deposited")
            return
        else:
            print("Making " + choice.name + ":")
            choice.make()
            self.cashBox.deduct(choice.get_prices())


class CoffeeMachine:
    def __init__(self):
        self.cashBox = CashBox()
        products = []
        products.append(Product("black", 35, "   Dispensing cup\n   Dispensing coffee\n   Dispensing water"))
        products.append(Product("white", 35, "   Dispensing cup\n   Dispensing coffee\n   Dispensing creamer\n   Dispensing water"))
        products.append(Product("sweet", 35, "   Dispensing cup\n   Dispensing coffee\n   Dispensing sugar\n   Dispensing water"))
        products.append(Product("white & sweet", 35, "   Dispensing cup\n   Dispensing coffee\n   Dispensing sugar\n   Dispensing creamer\n   Dispensing water"))
        products.append(Product("bouilon", 25, "   Dispensing cup\n   Dispensing bouillon powder\n   Dispensing water"))
        self.selector = Selector(self.cashBox, products)

    def one_action(self):
        print("__________________________________________________________ \n   PRODUCT LIST: all 35 cents, except bouillon (25 cents) \n   1=black, 2=white, 3=sweet, 4=white & sweet, 5=bouillon \n   Sample commands: insert 25, select 1.")
        resp = input("Your command: ")
        resp = resp.split()

        if resp[0] == "quit":
            return False
        if resp[0] == "cancel":
            self.cashBox.return_coins()
            self.one_action()
        elif resp[0] == "insert":
            self.cashBox.deposit(int(resp[1]))
            self.one_action()
        elif resp[0] == "select":
            self.selector.select(int(resp[1]))
            self.one_action()
        else:
            print("Invalid command.")
            self.one_action()
    

    def totalCash(self):
        totalCash = self.cashBox.total_cash
        return totalCash

def main():
    m = CoffeeMachine()
    while m.one_action():
        pass
    total = m.totalCash()
    print(f"Total cash received: ${total/100:.2f}")

if __name__ == "__main__":
    main()
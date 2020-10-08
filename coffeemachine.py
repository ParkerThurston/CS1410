
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
        self.credit = 0.0
        self.total_cash = 0.0

    def deposit(self, amount):
        self.total_cash += amount

    def return_coins(self):
        #returns int
        pass
    
    def have_you(self, amount):
        #return bool
        pass

    def deduct(self, amount):
        pass

    def total(self):
        Mola = self.total_cash
        return Mola

        

class Selector:
    def __init__(self, cashbox):
        self.cashBox = cashbox
        self.products = ["black", 35, "white", 35, "sweet", 35, "white & sweet", 35, "bouillon", 25]

    def select(self, choice):
        pass
        

class CoffeeMachine:
    def __init__(self):
        #self.totalC = 0.0
        self.cashBox = CashBox()
        self.selector = Selector(self.cashBox)

    def one_action(self):
        print("__________________________________________________________ \n   PRODUCT LIST: all 35 cents, except bouillon (25 cents) \n   1=black, 2=white, 3=sweet, 4=white & sweet, 5=bouillon \n   Sample commands: insert 25, select 1.")
        resp = input("Your command: ")

        resp = resp.split()

        if resp[0] == "quit":
            return False
        if resp[0] == "cancel":
            print("Returning "+str(int(self.cashBox.credit)) +" cents.")
            self.one_action()
        elif resp[0] == "insert":
            if resp[1] == "50" or resp[1] == "25" or resp[1] == "10" or resp[1] == "5":
                credit = int(resp[1])
                self.cashBox.credit += credit
                self.cashBox.deposit(credit)
                print("Depositing " +resp[1]+" cents. You Have " +str(int(self.cashBox.credit))+ " cents credit.")
                self.one_action()
            else:
                print("INVALID AMOUNT")
        elif resp[0] == "select":
            pass
            #if self.cashBox.credit < self.selector.# ??? price
        else:
            print("Invalid entry")

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
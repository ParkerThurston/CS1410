
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
        #retAmount = self.credit
        self.total_cash -= self.credit
        retAmount = self.total_cash
        return retAmount
    
    def have_you(self, amount):
        if amount <= self.credit:
            return True
        else:
            return False

    def deduct(self, amount):
        self.credit -= amount
        print("Returning " +str(self.credit)+ " cents.")

    def total(self):
        Mola = self.total_cash
        return Mola

        

class Selector:
    def __init__(self, choice):
        self.cashBox = CashBox()
        self.products = ["Filler","Black", 35, "White", 35, "Sweet", 35, "White & Sweet", 35, "Bouillon", 25]
        self.recipe = {"1":"   Dispensing Cup\n   Dispensing Coffee\n   Dispensing Water", 
                    "2":    "Dispensing Cup\n   Dispensing Coffee\n   Dispensing Creamer\n   Dispensing Water", 
                    "3":    "Dispensing Cup\n   Dispensing Coffee\n   Dispensing Sugar\n   Dispensing Water"}
    def select(self, choice):
        if choice == "1" or choice == "2" or choice == "3" or choice == "4":
            #if self.cashBox.have_you(35) == True:
            self.product = Product(str(self.products[int(choice)]), str(self.products[int(choice)*2]), str(self.recipe[choice]))
            print("Making " +(self.product.name)+":")
            self.product.make()
            self.cashBox.deduct(int(self.products[int(choice)*2]))
            self.cashBox.return_coins()
        
        #   else:
        #         print("F")
        #elif choice == "5":
        #     pass
        else:
            print(choice + " is not an option, Try again.")
            

        

class CoffeeMachine:
    def __init__(self):
        self.cashBox = CashBox()
        self.selector = Selector(None)

    def one_action(self):
        print("__________________________________________________________ \n   PRODUCT LIST: all 35 cents, except bouillon (25 cents) \n   1=black, 2=white, 3=sweet, 4=white & sweet, 5=bouillon \n   Sample commands: insert 25, select 1.")
        resp = input("Your command: ")

        resp = resp.split()

        if resp[0] == "quit":
            return False
        if resp[0] == "cancel":
            amount = self.cashBox.return_coins()
            print("Returning "+ str(int(amount)) +" cents.")
            self.cashBox.credit = 0.0
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
            selection = resp[1]
            if selection == "1" or selection =="2" or selection == "3" or selection == "4" or selection == "5":
                self.selector.select(selection)
            else:
                print(selection + "is not an option, try again.") 
                self.one_action()   
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
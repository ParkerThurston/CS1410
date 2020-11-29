#Code written by Parker Thurston with help from Class (With some extra help from Hannah Young)
from abc import ABC, abstractmethod

class Employee:
    def __init__(self, emp_id, first_name, last_name, address, city, state, zipcode):
        self.emp_id = emp_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self. state = state
        self.zipcode = zipcode
        self.classification = None
    
    def get_employee_id(self):
        return self.emp_id  

    def make_hourly(self, rate):
        self.classification = Hourly(rate)

    def make_salaried(self, salary):
        self.classification = Salarised(salary)
        

    def make_commissioned(self, salary, rate):
        self.classification = Commissioned(salary, rate)
        

    def issue_payment(self):
        with open("paylog.txt", "a") as f:
            f.write("Mailing "+ str(self.classification.compute_pay())+" to " + self.first_name+" "+ self.last_name+" " + self.address +" "+ self.city+ " " + self.state + " "+ self.zipcode + "\n")

        
        
    
    
class Classification:
    def __init__(self):
        emp = Employee()

    @abstractmethod
    def compute_pay(self):
        pass




class Hourly(Classification):
    def __init__(self,hourly_rate):
        self.hourly_rate = hourly_rate
        self.timecard = []

    def add_timecard(self, card):
        self.timecard.append(card)

    def compute_pay(self):
        total_hours_worked = 0
        count = 0
        for hours in self.timecard:
            total_hours_worked += float(hours)
            self.timecard[count] = 0
            count += 1
            

        return round(total_hours_worked * float(self.hourly_rate), 2)

class Salarised(Classification):
    def __init__(self, salary):
        self.salary = salary

    def compute_pay(self):
        return round(float(self.salary) / 24 ,2)
        
        

class Commissioned(Classification):
    def __init__(self, salary, commission_rate):
        self.salary = salary
        self.commission_rate = commission_rate
        self.receipts = []

    def add_receipt(self, amount):
        self.receipts.append(amount)

    def compute_pay(self):
        total_receipts_pay = 0
        count = 0
        for sales in self.receipts:
            total_receipts_pay += ((float(self.commission_rate)/100) * float(sales))
            self.receipts[count] = 0
            count += 1
            

        tfthSal = (float(self.salary) / 24) 
        return round(tfthSal + total_receipts_pay,2)

         
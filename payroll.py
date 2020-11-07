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
    
    def make_hourly(self, rate):
        self.classification = Hourly(rate)

    def make_salarised(self, salary):
        #self.classification = Salaried(salary)
        pass

    def make_commissioned(self, salary, rate):
        #self.classification = Commissioned(salary, rate)
        pass
    
    
class Classification:
    def __init__(self):
        emp = Employee()

    @abstractmethod
    def issue_payment(self):
        pass


class Hourly(Classification):
    def __init__(self,hourly_rate):
        self.hourly_rate = hourly_rate
        self.timecard = []

    def add_timecard(self, card):
        self.timecard.append(card)

    def compute_pay(self):
        total_hours_worked = 0
        for hours in self.timecard:
            total_hours_worked += hours

        return round(total_hours_worked * self.hourly_rate, 2)

class Salarised(Classification):
    def __init__(self, salary):
        self.salary = salary

    def compute_pay(self):
        return round(self.salary / 24)
        
        

class Commissioned(Classification):
    def __init__(self, salary, rate):
        self.salary = salary
        self.commission_rate = commission_rate
        self.receipts = []

    def add_receipt(self, amount):
        pass

    def compute_pay(self):
        pass
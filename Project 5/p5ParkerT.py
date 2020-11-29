#Code written by Parker Thurston with help from Class (With some extra help from Hannah Young)
'''
    p5.py: Illustrates the payroll module.
'''

from payroll import *
import os, os.path, shutil

PAY_LOGFILE = 'paylog.txt'
employees = []

def load_employees():
    with open("employees.csv", "r") as reader:
        reader.readline()

        while reader:
            emp = reader.readline().strip().split(',')
            if emp[0] == "":
                return
            new_emp = Employee(emp[0], emp[1], emp[2], emp[3], emp[4], emp[5], emp[6])

            if emp[7] == "3": #Hourly Emp
                new_emp.make_hourly(emp[10])
            elif emp[7] == "2": #Commissioned Emp
                new_emp.make_commissioned(emp[8], emp[9])
            else: # Salaried Emp
                new_emp.make_salaried(emp[8])

            employees.append(new_emp)

def process_timecards():
    with open("timecards.csv", "r") as reader:
        
        while reader:
            timecard = reader.readline().strip().split(',')
            if timecard[0] =="":
                return

            employ = find_employee_by_id(timecard[0])
            if employ != None:
                for i in range(1,len(timecard)):
                    employ.classification.add_timecard(timecard[i])


def process_receipts():
    with open("receipts.csv", "r") as reader:

        while reader:
            receipt = reader.readline().strip().split(',')
            if receipt[0] == "":
                return
            employ = find_employee_by_id(receipt[0])
            if employ != None:
                for i in range(1,len(receipt)):
                    employ.classification.add_receipt(receipt[i])
                


def run_payroll():
    if os.path.exists(PAY_LOGFILE):          # pay_log_file is a global variable holding ‘payroll.txt’
        os.remove(PAY_LOGFILE)
    for emp in employees:          # employees is the global list of Employee objects
        emp.issue_payment()


def find_employee_by_id(number):
    for emp in employees:
        emp_id = emp.get_employee_id()
        if emp_id == number:
            return emp
    return None
        

    
def main():
    load_employees()
    process_timecards()
    process_receipts()
    run_payroll()

    # Save copy of payroll file; delete old file
    shutil.copyfile(PAY_LOGFILE, 'paylog_old.txt')
    if os.path.exists(PAY_LOGFILE):
        os.remove(PAY_LOGFILE)

    # Change Issie Scholard to Salaried by changing the Employee object:
    emp = find_employee_by_id('51-4678119')
    emp.make_salaried(134386.51)
    emp.issue_payment()

    # Change Reynard,Lorenzin to Commissioned; add some receipts
    emp = find_employee_by_id('11-0469486')
    emp.make_commissioned(50005.50, 27)
    clas = emp.classification
    clas.add_receipt(1109.73)
    clas.add_receipt(746.10)
    emp.issue_payment()

    # Change Jed Netti to Hourly; add some hour entries
    emp = find_employee_by_id('68-9609244')
    emp.make_hourly(47)
    clas = emp.classification
    clas.add_timecard(8.0)
    clas.add_timecard(8.0)
    clas.add_timecard(8.0)
    clas.add_timecard(8.0)
    clas.add_timecard(8.0)
    emp.issue_payment()

if __name__ == '__main__':
    main()

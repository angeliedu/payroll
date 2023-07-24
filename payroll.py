
from Employee import Employee
from Veichle import Veichle
from EmployeeFT import EmployeeFT
from EmployeePT import EmployeePT
from EmployeeINTL import EmployeeINTL

class Payroll:
    employeeFT_list = []
    employeePT_list = []
    employeeINTL_list = []

    @classmethod
    def main_loop(cls):
        while True:
            name = input("Please enter name (or '999' to exit): ")
            if name == "999":
                cls.display_all_employees()
                break
            ID = input("Enter ID: ")
            age = int(input("Enter your age: "))

            # Check if the employee has a car
            car_option = int(input("Enter if you have a car (1 to have a car or 2 no have car): "))
            V1 = None
            if car_option == 1:
                make = input("Enter who make the car: ")
                model = input("Enter model of the car: ")
                V1 = Veichle()
                V1.make = make
                V1.model = model

            # Type of Employee
            employee_type = int(input("Enter type of employee (1 for Full-Time, 2 for Part-Time, 3 for Intern): "))
            if employee_type == 1:  # Full-Time Employee
                salary = float(input("Enter salary: "))
                bonus = float(input("Enter bonus: "))
                emp = EmployeeFT()
                emp.name = name
                emp.age = age
                emp.ID = ID  
                emp.salary = salary
                emp.bonus = bonus
                emp.V1 = V1
                cls.employeeFT_list.append(emp)

            elif employee_type == 2:  # Part-Time Employee
                rate = float(input("Enter rate of pay: "))
                hours = float(input("Enter hours worked: "))
                emp = EmployeePT()
                emp.name = name
                emp.age = age
                emp.ID = ID  
                emp.ratepay = rate
                emp.hourswork = hours
                emp.V1 = V1
                cls.employeePT_list.append(emp)

            elif employee_type == 3:  # Intern Employee
                stipend = float(input("Enter stipend: "))
                emp = EmployeeINTL()
                emp.name = name
                emp.age = age
                emp.ID = ID
                emp.stipend = stipend
                emp.taxes = 50.00
                emp.V1 = V1
                cls.employeeINTL_list.append(emp)

    @classmethod
    def display_all_employees(cls):
        print("\nFull-Time Employees:")
        for emp in cls.employeeFT_list:
            car_info = f", Car: {emp.V1.make} {emp.V1.model}" if emp.V1 else ""
            print(f"Name: {emp.name}, ID: {emp.ID}, Age: {emp.age}{car_info}, Salary: {emp.salary}, Bonus: {emp.bonus}")
        
        print("\nPart-Time Employees:")
        for emp in cls.employeePT_list:
            car_info = f", Car: {emp.V1.make} {emp.V1.model}" if emp.V1 else ""
            print(f"Name: {emp.name}, ID: {emp.ID}, Age: {emp.age}{car_info}, Rate of Pay: {emp.ratepay}, Hours Worked: {emp.hourswork}")

        print("\nIntern Employees:")
        for emp in cls.employeeINTL_list:
            car_info = f", Car: {emp.V1.make} {emp.V1.model}" if emp.V1 else ""
            print(f"Name: {emp.name}, ID: {emp.ID}, Age: {emp.age}{car_info}, Taxes: {emp.taxes}, Stipend: {emp.stipend - emp.taxes}")


if __name__ == "__main__":
    Payroll.main_loop()

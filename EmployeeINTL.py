from Employee import Employee

class EmployeeINTL(Employee):  
    def __init__(self):
        super().__init__()
        self.stipend = 0.0
        self.taxes = 50.00
    
    def calc_earnings(self):
        return self.stipend - self.taxes
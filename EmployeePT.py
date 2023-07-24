from Employee import Employee

class EmployeePT(Employee):
    def __init__(self):
        super().__init__()
        self.ratepay = 0.0
        self.hourswork = 0.0
        self.earnings = 0.0
    
    def calc_earnings(self):
        return self.hourswork * self.ratepay
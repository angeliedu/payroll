from Employee import Employee


class EmployeeFT(Employee): 
    def __init__(self):
        super().__init__()  # Call the parent class's constructor
        self.salary = 0.0
        self.bonus = 0.0
        self.earnings = 0.0
    
    def calc_earnings(self):
        return self.salary + self.bonus

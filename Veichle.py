from Employee import Employee

class Veichle(Employee):  # Inherit from Employee
    def __init__(self):
        super().__init__()
        self.make = ""
        self.model = ""

class Employee:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(f"Tên nhân viên: {self.name}")
class Date_of_birth(Employee):
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        print(f"Ngày vào: {self.day}/{self.month}/{self.year}")
class Date_in(Employee):
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        print(f"Ngày sinh: {self.day}/{self.month}/{self.year}")

obj1 = Employee("Pham Ha Nam")
date1= Date_of_birth(11,4,2004)
date2= Date_in(21,5,2026)
obj1.display()
date1.display()
date2.display()

    
    
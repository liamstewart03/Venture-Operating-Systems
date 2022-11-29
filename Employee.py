import datetime;

class Employee:

    def __init__(self, name, age, start_date, cars_sold, total_profits):
    
        self.name = name
        self.age = age
        self.start_date = start_date
        self.age = age
        self.cars_sold = cars_sold
        self.total_profits = total_profits
        self.calculate_commissions_rate()
        self.calculate_employee_commissions()

    def __str__(self):
        return f"""
        Name: {self.name}
        Age: {self.age}
        Start Date: {self.start_date}
        Biography: {self.bio}
        Cars Sold: {self.cars_sold}
        Total Profits: {self.total_profits}
        Employee Profits: {self.employee_commissions}
        """

    #increments the amount of cars sold by one
    def increment_cars_sold(self):
        self.cars_sold += 1

    #sets the commission rate
    def calculate_commissions_rate(self):
        if self.cars_sold <= 8:
            self.commission_rate = 0.13
        elif 8 >= self.cars_sold <= 10:
            self.commission_rate = 0.15
        elif 11 >= self.cars_sold <= 13:
            self.commission_rate = 0.2
        elif self.cars_sold >= 15:
            self.commission_rate = 0.25

    #sets the amount of commission made
    def calculate_employee_commissions(self):
        self.employee_commissions = self.total_profits * self.commission_rate


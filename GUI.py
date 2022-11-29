import tkinter as tk
from tkinter import messagebox
from Employee import *
from Car import *


class GUI:

    def __init__(self):
        #initialize root window
        self.root = tk.Tk()
        self.root.geometry("1000x1000")
        self.root.title("Venture Operating Systems")
        #create button frame
        self.buttonframe = tk.Frame(self.root)
        self.buttonframe.columnconfigure(0, weight=1) 
        self.buttonframe.columnconfigure(1, weight=1)
        #create and place employee button
        self.employee_button = tk.Button(self.buttonframe, text="Employees", font=('Arial', 40), width=1, height=10, command=self.open_employee_window)
        self.employee_button.grid(row=0, column=0, sticky=tk.E+tk.W)
        #create and place car button
        self.car_button = tk.Button(self.buttonframe, text="Cars", font=('Arial', 40), width=1, height=10, command=self.open_car_window)
        self.car_button.grid(row=0, column=1, sticky=tk.E+tk.W)
        #pack button frame in root
        self.buttonframe.pack(pady=10, fill=tk.X)

        self.root.mainloop()

    def open_employee_window(self):
    
        #initialize employee window
        self.employee_window = tk.Tk()
        self.employee_window.title("Employees")
        self.employee_window.geometry("1000x1000")
        #create scrollbar and place it in employee window
        self.scrollbar = tk.Scrollbar(self.employee_window)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        #create listbox that allows scrolling
        self.employee_list = tk.Listbox(self.employee_window, yscrollcommand = self.scrollbar.set)
        employee_names = ["Kaden Range", "Nathan Miller", "Patrick Koury", "Neil Correia", "Liam Stewart", "Kendal Kelly", "Marco Lawrence", "Anabella Hendrix", "Corinne Hammond", "Elizabeth Drake", "Adyson Day", "Dillan Alexander", "Adison Figueroa", "Angeline Vasquez", "Todd Baldwin", "Makaila Watkins", "Ramiro Perkins"]
        for name in employee_names:
            self.employee_list.insert(tk.END, name)
        self.employee_list.pack(side=tk.TOP, fill=tk.X)
        self.scrollbar.config(command = self.employee_list.yview )
        #create label for entry
        self.label = tk.Label(self.employee_window, text="Enter Employee Name", font=('Arial', 18, 'bold'))
        self.label.pack(anchor='nw')
        #create entry
        self.employee_name_entry = tk.Entry(self.employee_window, font=('Arial', 18))
        self.employee_name_entry.pack(anchor='nw')
        #create submit button that takes information from entry
        self.employee_submit_button = tk.Button(self.employee_window, text="Submit", font=('Arial', 18), command=self.open_employee)
        self.employee_submit_button.pack(anchor='nw')

        self.employee_window.mainloop()

        
    def open_employee(self):
            if self.employee_name_entry.get() == "":
                messagebox.showerror(message="Please enter an employee name")
            else:    
                if self.employee_name_entry.get().lower() == "kaden range":
                    self.employee = Employee("Kaden Range", 18, "09/09/22", 11, 330000)

                elif self.employee_name_entry.get().lower() == "nathan miller":
                    self.employee = Employee("Nathan Miller", 18, "07/21/22", 11, 345000)

                elif self.employee_name_entry.get().lower() == "patrick koury":
                    self.employee = Employee("Patrick Koury", 19, "10/24/22", 9, 315000)
                    
                elif self.employee_name_entry.get().lower() == "neil correia":
                    self.employee = Employee("Neil Correia", 19, "06/15/22", 10, 350000)

                elif self.employee_name_entry.get().lower() == "liam stewart":
                    self.employee = Employee("Liam Stewart", 19, "11/22/22", 7, 246000)

                self.create_employee_info_window()
                

    def create_employee_info_window(self):

        self.employee_info_window = tk.Tk()
        self.employee_info_window.title(f"{self.employee.name}'s Info")
        self.employee_info_window.geometry('1000x1000')

        self.info_frame = tk.Frame(self.employee_info_window)
        self.info_frame.columnconfigure(0, weight=1)
        self.info_frame.columnconfigure(1, weight=1)

        self.age_button = tk.Button(self.employee_info_window, text="Age", font=("Arial", 18), command=self.show_age, height=5)
        self.age_button.grid(row=0, column=0, sticky="nswe")

        self.start_date_button = tk.Button(self.employee_info_window, text="Start Date", font=("Arial", 18), command=self.show_start_date, height=5)
        self.start_date_button.grid(row=1, column=0, sticky="nswe")

        self.cars_sold_button = tk.Button(self.employee_info_window, text="Cars Sold", font=("Arial", 18), command=self.show_cars_sold, height=5)
        self.cars_sold_button.grid(row=2, column=0, sticky="nswe")
        
        self.commission_rate_button = tk.Button(self.employee_info_window, text="Commission Rate", font=("Arial", 18), command=self.show_commission_rate, height=5)
        self.commission_rate_button.grid(row=3, column=0, sticky="nswe")

        self.total_profits_button = tk.Button(self.employee_info_window, text="Total Profits", font=("Arial", 18), command= self.show_total_profits, height=5)
        self.total_profits_button.grid(row=4, column=0, sticky="nswe")

        self.employee_commisions_button = tk.Button(self.employee_info_window, text="Employee Commissions", font=("Arial", 18), command=self.show_employee_commissions, height=5)
        self.employee_commisions_button.grid(row=5, column=0, sticky="nswe")

        self.age_entry = tk.Entry(self.employee_info_window, font=("Arial", 18), state="disabled")
        self.age_entry.grid(row=0, column=1)
        
        self.start_date_entry = tk.Entry(self.employee_info_window, font=("Arial", 18), state="disabled")
        self.start_date_entry.grid(row=1, column=1)

        self.cars_sold_entry = tk.Entry(self.employee_info_window, font=("Arial", 18), state="disabled")
        self.cars_sold_entry.grid(row=2, column=1)

        self.commission_rate_entry = tk.Entry(self.employee_info_window, font=("Arial", 18), state="disabled")
        self.commission_rate_entry.grid(row=3, column=1)

        self.total_profits_entry = tk.Entry(self.employee_info_window, font=("Arial", 18), state="disabled")
        self.total_profits_entry.grid(row=4, column=1)

        self.employee_commissions_entry = tk.Entry(self.employee_info_window, font=("Arial", 18), state="disabled")
        self.employee_commissions_entry.grid(row=5, column=1)

        self.info_frame.pack()

        self.employee_info_window.mainloop()
    
    def show_age(self):
        self.age_entry.configure(state="normal")
        self.age_entry.delete(0, tk.END)
        self.age_entry.insert(0, self.employee.age)

    def show_start_date(self):
        self.start_date_entry.configure(state="normal")
        self.start_date_entry.delete(0, tk.END)
        self.start_date_entry.insert(0, self.employee.start_date)

    def show_cars_sold(self):
        self.cars_sold_entry.configure(state="normal")
        self.cars_sold_entry.delete(0, tk.END)
        self.cars_sold_entry.insert(0, self.employee.cars_sold)

    def show_commission_rate(self):
        self.commission_rate_entry.configure(state="normal")
        self.commission_rate_entry.delete(0, tk.END)
        self.commission_rate_entry.insert(0, f"{int(self.employee.commission_rate * 100)}%")
        

    def show_total_profits(self):
        self.total_profits_entry.configure(state="normal")
        self.total_profits_entry.delete(0, tk.END)
        self.total_profits_entry.insert(0, self.employee.total_profits)

    def show_employee_commissions(self):
        self.employee_commissions_entry.configure(state="normal")
        self.employee_commissions_entry.delete(0, tk.END)
        self.employee_commissions_entry.insert(0, int(self.employee.employee_commissions))

    def show_all(self):
        self.show_age()
        self.show_start_date()
        self.show_cars_sold()
        self.show_commission_rate()
        self.show_total_profits()
        self.show_employee_commissions()

        

    def open_car_window(self):
        self.car_window = tk.Tk()
        self.car_window.title("Cars")
        self.car_window.geometry("1000x1000")

        self.car_window_button_frame = tk.Frame(self.car_window)
        self.car_window_button_frame.columnconfigure(0, weight=1)
        self.car_window_button_frame.columnconfigure(1, weight=1)
        self.car_window_button_frame.columnconfigure(2, weight=1)

        self.SUV_button = tk.Button(self.car_window_button_frame, text="SUVs", font=("Arial", 18), height=5, command=self.open_SUV_window)
        self.SUV_button.grid(row=0, column=0, sticky=tk.W+tk.E)

        self.sedan_button = tk.Button(self.car_window_button_frame, text="Sedans", font=("Arial", 18), height=5, command=self.open_sedan_window)
        self.sedan_button.grid(row=0, column=1, sticky=tk.W+tk.E)

        self.wagon_button = tk.Button(self.car_window_button_frame, text="Wagons", font=("Arial", 18), height=5, command=self.open_wagon_window)
        self.wagon_button.grid(row=0, column=2, sticky=tk.W+tk.E)
        
        self.coupe_button = tk.Button(self.car_window_button_frame, text="Coupes", font=("Arial", 18), height=5, command=self.open_coupe_window)
        self.coupe_button.grid(row=1, column=0, sticky=tk.W+tk.E)

        self.convertible_button = tk.Button(self.car_window_button_frame, text="Convertibles", font=("Arial", 18), height=5, command=self.open_convertible_window)
        self.convertible_button.grid(row=1, column=1, sticky=tk.W+tk.E)

        self.electric_button = tk.Button(self.car_window_button_frame, text="Electric Cars", font=("Arial", 18), height=5, command=self.open_electric_window)
        self.electric_button.grid(row=1, column=2, sticky=tk.W+tk.E)

        self.car_window_button_frame.pack(fill=tk.X)

        self.car_window.mainloop()

    def open_SUV_window(self):
        self.cars = [Car("SUV", "GLA SUV", 37500), Car("SUV", "GLB SUV", 38600), Car("SUV", "GLC SUV", 43850), Car("SUV", "GLC Coupe", 52500),Car("SUV", "GLE SUV", 56150), Car("SUV", "GLE COUPE", 78450), Car("SUV", "GLS SUV", 77850), Car("SUV", "G-CLASS SUV", 139900), Car("SUV", "Mercedes-Maybach GLS SUV", 165100)]
        self.create_subcar_window()

    def open_sedan_window(self):
        self.cars = [Car("Sedan", "A-Class Sedan", 33950), Car("Sedan", "C-Class Sedan", 43550), Car("Sedan", "E-Class Sedan", 54950), Car("Sedan", "S-Class Sedan", 111100), Car("Sedan", "Mercedes-Maybach S-Class", 184900)]
        self.create_subcar_window()
        
    def open_wagon_window(self):
        self.cars = [Car("Sedan", "Mercedes-Maybach S-Class", 184900)]
        self.create_subcar_window()

    def open_coupe_window(self):
        self.cars = [Car("Coupe", "CLA Coupe", 39350), Car("Coupe", "C-Class Coupe", 47850), Car("Coupe", "E-Class Coupe", 66100), Car("Coupe", "CLS Coupe", 72950), Car("Coupe", "Mercedes-AMG GT 4-door Coupe", 92500), Car("Coupe", "Mercedes-AMG GT", 118600)]
        self.create_subcar_window()

    def open_convertible_window(self):
        self.cars = [Car("Convertible", "C-Class Cabriolet", 55400), Car("Convertible", "E-Class Cabriolet", 73250), Car("Roadster", "SL Roadster", 137400)]
        self.create_subcar_window()

    def open_electric_window(self):
        self.cars = [Car("Electric", "EQB SUV", 54500), Car("Electric", "EQS Sedan", 102310), Car("Electric", "EQS SUV", 104400)]
        self.create_subcar_window()

    def create_subcar_window(self):
        self.subcar_window = tk.Tk()
        self.subcar_window.title("SUVs")
        self.subcar_window.geometry("1000x1000")


        self.subcar_window_scrollbar = tk.Scrollbar(self.subcar_window)
        self.subcar_window_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.car_list = tk.Listbox(self.subcar_window, yscrollcommand = self.subcar_window_scrollbar.set)
        
        line = 1
        for car in self.cars:
            self.car_list.insert(tk.END, f"{str(line)}: {car.model}")
            line += 1
            
        
        self.car_list.pack(side=tk.TOP, fill=tk.X)
        self.subcar_window_scrollbar.config(command = self.car_list.yview)

        self.entry_label = tk.Label(self.subcar_window, text="Enter Number", font=("Arial", 18, "bold"))
        self.entry_label.pack(anchor='nw')

        self.number_entry = tk.Entry(self.subcar_window)
        self.number_entry.pack(anchor='nw')

        self.price_button = tk.Button(self.subcar_window, text="Get Price", font=("Arial", 18), command=self.show_price)
        self.price_button.pack(anchor='nw')

        

        
        
        self.subcar_window.mainloop()

        
    def show_price(self):
        if self.check_state == 0:
            messagebox.showinfo(title="Car Price", message=self.cars[int(self.number_entry.get()) - 1].price)
        if self.check_state == 1:
            messagebox.showinfo(title="Car Price", message=self.cars[int(self.number_entry.get()) - 1].price * .97)


GUI()


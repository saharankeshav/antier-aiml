# class A:
#    def fun(self,name):
#          self.name = name
#          print("her name is ", name)

#    def show(self,age):
#         print(self.name , "is" , age , "year old")
 
# obj = A()
# obj.fun("Riya")
# obj.show(10)

# class name = caluclations
# inside class -> fun named circle that takes radius as input . 
# another function calulation_area that caluclate area of circle



# class Calculation:
#     def fun(self, circle):
#         print("Radius is", circle)

#     def calculation_area(self, circle):
#         area = 3.14 * circle ** 2
#         print("Area of circle is", area)


# obj = Calculation()
# obj.fun(7)
# obj.calculation_area(7)


# class Employee:
#     def set_salary(self,basic_salary):
#         print("Current salary is " , basic_salary)

#     def calculate_bonus(self,basic_salary):
#             salary = (basic_salary*10/100 + basic_salary)
#             print("After Bonus: " , salary)
            




# obj = Employee()
# obj.set_salary(10000)
# obj.calculate_bonus(10000)



class BankAccount:
    def __init__(self):
        self.balance = 1000        # one shared variable for all functions

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposited:", amount, "| Current Balance:", self.balance)

    def withdraw(self, amount):
            self.balance = self.balance - amount
            print("Withdrawn:", amount, "| Remaining Balance:", self.balance)

    def show_balance(self):
        print("Account Balance:", self.balance)


obj = BankAccount()
obj.deposit(1000)
obj.withdraw(500)
obj.show_balance()





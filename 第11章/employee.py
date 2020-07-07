'''这是11-3的练习题'''

class Employee():
    def __init__(self,last_name,first_name,annualsalary):
        self.last_name = last_name
        self.first_name = first_name
        self.annualsaalary = annualsalary

    def give_raise(self,addanual=5000):#给形参一个初始值
         self.annualsaalary  += addanual
         print(self.annualsaalary)


class Employee:
    def __init__(self, emp_id,name,salary):
        self.emp_id=emp_id
        self.name=name
        self.salary=salary 
        
    def calculate_salary(self):
        pass
    
     
class hourlyEmployee(Employee):
    def __init__(self,emp_id,name,salaryhourly_rate,hours_worked):
        super().__init__(self,emp_id,name,salary)   
        self.hourly_rate=hourly_rate 
        self.hours_worked=hours_worked
    
    def calculate_salary (self):
        calculate_salary=(hourly_rate*hours_worked) +commission 
    
        pass
class salaried_employee(Employee):
     def __init__(self,emp_id,name,salary, monthly_salary ):
         super ().__init__(self,emp_id,name,salary)
         self.monthly_salary=monthly_salary 
         
     def calculate_salary (self) :
    
         pass
         
print

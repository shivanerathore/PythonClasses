#Shivane Rathore
#Employee Managment System (ems) class

import pickle
from employee import Employee

class EmployeeManagementSystem :
   def __init__(self):
       try:
           fp = open("empPickle","rb")
           self.emp = pickle.load(fp)
           fp.close() 
       except IOError:
           self.emp = {}
          
   #looking up  
   def search_employee(self):
       id = input("Enter an employee ID number: ")
       if id in self.emp.keys():
           print(self.emp[id])
       else:
           print("The specified ID number was not found")
       print(" ")
          
   #adding    
   def add_employee(self):
       name = input("Enter employee name: ")
       id = input("Enter employee ID number: ")
       department = input("Enter employee department: ")
       title = input("Enter employee title: ")
       if id in self.emp.keys():
           print("The specified ID number already exists. Please try to edit the employee")
       else:
           self.emp[id] = Employee(id,name,department,title)
           print("The new employee has been added.")
       print(" ")
          
   #updating  
   def update_employee(self):
       id = input("Enter employee ID number: ")
       if id not in self.emp.keys():
           print("The specified ID number was not found. ")
       else:
           name = input("Enter the new name: ")
           department = input("Enter the new department: ")
           title = input("Enter the new title: ")
           self.emp[id].set_name(name)
           self.emp[id].set_department(department)
           self.emp[id].set_job_title(title)
           print("Employee information updated.")
       print(" ")

   #deleting    
   def delete_employee(self):
       id = input("Enter employee ID number: ")
       if id in self.emp.keys():
           del self.emp[id]
           print("Employee information deleted.")
       else:
           print("The specified ID number was not found")
       print(" ")
          
   #displaying 
   def display_employees(self):
       print("{0} {1} {2} {3}".format("Name", "ID Number", "Department", "Job Title"))
       for id in self.emp.keys():
           print(self.emp[id])
       print(" ")
          
   #displaying menu choices
   def menu(self):
       while True:
           print("Menu")
           print("-"*50)
           print("1. Look up an employee")
           print("2. Add a new employee")
           print("3. Change an existing employee")
           print("4. Delete an employee")
           print("5. Output all employees' information on a table")
           print("6. Quit the program")
           choice = int(input("Enter your choice: "))
           if choice == 1:
               self.search_employee()
           elif choice == 2:
               self.add_employee()
           elif choice == 3:
               self.update_employee()
           elif choice == 4:
               self.delete_employee()
           elif choice == 5:
               self.display_employees()
           elif choice == 6:
               fp = open("empPickle","wb")
               pickle.dump(self.emp,fp)
               fp.close()
               break
           else:
               print("Invalid choice")
       
def main():
   EmployeeManagementSystem().menu()

main()  

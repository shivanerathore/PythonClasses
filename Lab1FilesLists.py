# Shivane Rathore
# Write a program that reads the "employees.txt" file that hold the information
# of employees in this order:
# - Name of the employee
# - Age of the employee
# - Salary of the employee
# Your program reads these information into different lists for each information, (e.g. name in names list) and print out/display the following information:
# - The lists for names, ages and salaries of the employees
# - Name of the employee that earns the least
# - Name of the employee that earns the most
# - Youngest employee name and salary
# - Oldest employee name and salary

# opening file
empFile = open("employees.txt", "r")

# making 3 different lists
nameList = []
ageList = []
salaryList = []

# while statement to get name, age salary in lists
while True:
    name = empFile.readline()
    age = empFile.readline()
    salary = empFile.readline()
    if not name:
        break
    nameList.append(name.strip())
    ageList.append(int(age.strip()))
    salaryList.append(int(salary.strip()))

# printing lists
print("Name:", nameList)
print("Age:", ageList)
print("Salary:",salaryList)

# max and min salary
mxSlry=max(salaryList)
mnSlry=min(salaryList)
print("The employee that earns the most:", nameList[salaryList.index(mnSlry)])
print("The employee that earns the least: ", nameList[salaryList.index(mxSlry)])

# max and min age
mxAge=max(ageList)
mnAge=min(ageList)
print("The oldest employee:", nameList[ageList.index(mxAge)]) 
print("The youngest employee:", nameList[ageList.index(mnAge)])

# closing the file
empFile.close()

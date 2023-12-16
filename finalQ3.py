#Shivane Rathore

class Employee:

    def __init__(self,name,empID,conStart,conTime):
        self.name = name
        self.num = num
        self.idNum = idNum
        self.conStart = conStart
        self.conTime = conTime
        
    #accessor and mutator for name
    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return (self.__make)

     #accessor and mutator for empID
    def set_empID(self, empID):
        self.__empID = empID
    def get_empID(self):
        if len(empID) > 6:
            return ("ID HAS TO BE LESS THAN 6 DIGITS!")
        return (self.__empID)

    #accessor and mutator for conStart
    def set_conStart(self, conStart):
        self.__conStart = str(conStart)
    def get_conStart(self):
        return (self.__conStart)

    #accessor and mutator for conTime
    def set_conTime(self, conTime):
        self.__conTime = int(conTime)
    def get_conTime(self):
        return (self.__conTime)



class PhysicianAssistant(Employee):
    
    def __init__(self,shiftNum):
        if shitNum == 1 or shiftNum == 2 or shiftNum == 3:
            self__.shift = shiftNum
        else:
            raise ValueError("CAN ONLY BE 1,2,or 3!!!!!")

    #accessor and mutator for shiftNum
    def set_shitNum(self,shiftNum):
        if shitNum == 1 or shiftNum == 2 or shiftNum == 3:
            self__.shift = shiftNum
        else:
            raise ValueError("CAN ONLY BE 1,2,or 3!!!!!")
    def get_shiftNum(self,shiftNum):
        if self.__shiftNum == 1:
            return ("first shift")
        if self.__shiftNUm == 2:
            return ("second shift")
        if self.__shiftNum == 3:
            return ("third shift")

#from Employee import name

while True:
    EMPname = input("Enter the Employee Name ")
    EMPID = input("Enter the Employee ID ")
    EMPSTART = input("Enter the Employee Contract Start Date ")
    EMPTIME = input("Enter the Employee Contracy Time ")
    break
    
emp = Employee(name,empID,conStart,conTime)
print("Employee Name: ", emp.get_name())
print("Employee Number: ", emp.get_empID())
print("Employee Contract Start Date: ", emp.get_conStart())
print("Employee Contract Time: ", emp.get_conTime())

pa = PhysicianAssistant(shiftNum)
print("Shift Number: ", pa.get_shiftNum())

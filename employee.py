#Shivane Rathore
#Employee class

class Employee:  
   def __init__(self, id, name, department, job_title):
       self.id = id
       self.name = name
       self.department = department
       self.job_title = job_title
      
   #returning string
   def __str__(self):
       return "{0} {1} {2} {3}".format(self.name, self.id, self.department, self.job_title)
      
   #updating department
   def set_department(self, department):
       self.department = department
      
   #updating names
   def set_name(self, name):
       self.name = name
  
   #updating job titles
   def set_job_title(self, title):
       self.job_title = title
              


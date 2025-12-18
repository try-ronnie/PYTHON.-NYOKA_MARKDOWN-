
# class Department is now the blueprint ... meaning it shows how the object will be build .... it just shows...
# but when its called thats when it actually creates the object according to the way we want
class Department ():
     # then we write a function that initializes the object to be created ... so this is where we 
     def __init__(self , name):
          self.name = name
          self.employees = []
    

d1 = Department('google')
print (d1)




class Employee :
     # what im getting is that in our initialization of employee we pass down department as an attribute ....
     # so what i think is that if it was an object it which would occur first or how does this occur 
     #another thing is that when we want to look into the memory or move its value somewhere we'd want to use self.name  .... this is like a read and paste only .... meaning it carries the value of name ..... but we cannot work on it if we wanted to....


     def __init__(self, name , position , department):
          self.name = name
          self.position = position
          self._department = department 
     #take the department arguement and picture it like the control panel ...... meaning it has 
     @property
     # this is the getter function that is attached to that panel for reading ..... 
     def department(self):
          return self.department
     @department.setter
     def department(self , department):
          if not isinstance(department , Department):
               print('department has to be an instance of the department class')
          self.department = department
          
engineering = Department('engineering')
Employee1 = Employee('edward' , 'head of mechanics' ,'mechanics')



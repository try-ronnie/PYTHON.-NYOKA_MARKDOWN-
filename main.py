# data structures and algorithms
class Student:
    def __init__(self, first_name, last_name):  
        self.first_nsme 

# note : onething is that classes name are defined using camelCase syntax
class User:
    user_list = [] # this list is to help us keep the data in one place as we create to make them iterable according to how they are called or tracked
    def __init__(self , name , gender):
        self.name = name
        self.gender = gender
        self.add_new_user(self)
    def __str__(self):
            return f'you are {self.name} and you are a {self.gender} '
    @classmethod
    def add_new_user(cls , new_user):
        cls.user_list.append(new_user)


use1 = User('titus' , 'male')
use2 = User('gikandi' , ' identifies as gay')
for users in User.user_list:
    print(users)


class Vehicle:
     def __init__(self, brand , model):
          self.model = model
          self.brand = brand
        
     def start(self):
          return ('vehicle is starting....')

class Subaru(Vehicle):
     def __init__(self, brand , wheel , model):
        super().__init__(brand,model)
        self.wheel = wheel
     def start(self):
          return (f'{self.brand} ')

u1 = Subaru('toyota' ,'x-trail' '6','2005' )
print(u1)


class Person:
     def __init__(self , name , age):
          self.name = name 
          self.__age = age 
    # we need to get a getter then set it in a setter 
     @property
     def age(self):
            return self.__age 
     # now this is the setter 
     @age.setter
     def age(self, value):
          if value > 0:
               print('value :' , value)
               self.__age = value
          else:
               print('invalid value')  


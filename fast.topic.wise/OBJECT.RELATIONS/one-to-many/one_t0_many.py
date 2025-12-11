# one to many refers to one parent object containing many children
# eg teachers -> many students belong to one class teacher 
#eg  shopper -> many grocery items one shopper may have bought 

class Shopper:

    def __init__(self , name):
        self.name = name
        self.grocery_items = []
        #we store an empty list that will be appended according to our will
        #NOTE we dont pass any attributes since we do not expect any value of groceries to be given when our object is created

class GroceryItem:
    def __init__ (self , name , price):
        self.name = name
        self.price = price


#first we create instances for this to work
shopper1 = Shopper('Alice')
grocery1 = GroceryItem('cabbage' , 250)
grocery2 = GroceryItem('cucumber' ,350)
#this is where we append the instances we've created
shopper1.grocery_items.append(grocery1)
shopper1.grocery_items.append(grocery2)

for item in shopper1.grocery_items:
    print(item.name , item.price)
# prints (cabbage 250 , cucumber 350)since we printed the objects created by grocery items in our shopper list since we appended them

#>>> two - way relationship
#for instance maybe a student would want to kknow something about their teacher class

class Student:
    # we need to store all the students we create
    all = []

    def _init__ (self , name , age):
        self.name = name
        self.age = age
        #teacher is protected since its not from the same constructor
        self._teacher = None
        Student.all.append(self)
    # we need to create getters for the student to know exactly who the teacher is ....
    @property
    def teacher (self):
        return self._teacher
    @teacher.setter
    def teacher (self , value ):
        if not isinstance(value, Teacher):
            raise TypeError('Teacher must be an instance of its class')
        else:
            self._teacher = value

class Teacher:
    def __init__(self , name):
        self.name = name

    #inorder to see how many students the teacher has
    def students(self):
        return [ students for students in Student.all if Student.teacher == self]
    # to add a new teacher to  a given student
    def add_student(self , value):
        if not isinstance(value , Student):
            raise TypeError('must be an instance of student')
        Student.teacher = self



class Author:
    def __init__ (self , name):
        self.name = name
    
class Book :
    # this is to store the instances of book we generate
    all = []
    def __init__(self , name , genre):
        self.name = name
        self.genre = genre
        # since its not from this class and we will need to update it later we made it protected 
        self._author = None
        Book.all.append(self)
    
    @property
    # getter method that returns the current value 
    # this also helps us get the value so we can update it accordingly
    def author(self):
        return self._author
    @author.setter
    def author(self , value):
        if not isinstance(value , Author):
            raise TypeError('make sure Author is an instance of its class')
    


class User:
    pupil = [] # class

    def __init__ (self, name):
        self.name = name
        User.pupil.append(name)

    def log_in(self):
        self.logged_in = True
    
class Student(User):
    def __init__(self, name , grade):
        super().__init__(name)
        self.grade = grade
        
        
    def log_in(self):
        super().log_in()# this calls the log_in from the parent
        self.in_class = True


s1 = Student('mumbi' , 'e')
print(Student.pupil)

# note that super() calls the method of the the parent 
# it allows us to add logic to the code if we want to change or add something without having to repeat the code of the parent method
#when you do super().__init__(name)
# you say hey python run the parents constructor method with the same self / attribute given
# this now pushes the name given in student as the name required in the parent since we run the initializing method in it
# super does not like pass the value it only takes the method behaviour and like copy pastes it to the sunclass
# meaning that 
def log_in(self):
        super().log_in()# this calls the log_in from the parent
        self.in_class = True

# here the we call user.log_In that just returns the value of being logged in as true  ... but for our student class it extends the behavoiur by just adding upon it
#super () just copy pastes the code that was supposed to be run in the parent and child
# super is just calls the method of the parent function inside the method of the subclass .... that is of the same name ......... well it doesnt have to be but you can
# super just lets you access the methods in the parent 


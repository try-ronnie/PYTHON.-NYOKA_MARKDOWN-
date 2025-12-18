class Employee:
    # this is a list where we will store all the instances of 
    #class-level
    all = [] #hook in to the class memory 
    def __init__(self, name ):
        #ANCHOR this is where we assign a department attribute that will be later reassigned a value so that every employee created will be then assigned later there department
        #ANCHOR Hence we need a getter and setter if we need to change the value afterwards

        self._department = None
        self.name = name 
        Employee.all.append(self)
    @property
    def department (self):
        return self._department
    @department.setter
    def department (self , value):
        # we then add a type check that checks whether the passed value is a direct instance of our Department class
        # if it is then reassign the value 
        # for a setter never use return as it only assigns a value 
        # but for getters you must return a value
        if isinstance(value , Department):
            self._department = value

    @classmethod

    def get_all_names(cls):
        return [employee.name for employee in Employee.all]
    
class Department:
    def __init__(self , name):
        self.name = name
    

    
a1 = Employee('patoranking')
a2 = Employee('gov.ronnie')
a3 = Employee('snowtina')
print(Employee.get_all_names())










count = [1,2,3,4,5]
def pato ():
    for num in count:
        print (num)
    return 
pato()
#NOTE print returns none .... so its not intended to be used in comprehensions since ut might return None upon runtime



# class Company:
#     pass


# pato = {'gender':"male", 'sex' :"gay"}
# print(pato['gender'])
class CarModel:
    def __init__(self , name):
        self.name = name

class CarCompany:
    def __init__ (self , name):
        self.name = name
        self.carmodels= []# has many instnaces of the carbrand they produce


    def car_brands_produced(self , carmodels):
        self.carmodels.append(carmodels)
# when we can poduce many carbrands ...
# we then get instance of carbrands as a list inside the object here as an attribute holding a list of the instances of the carbrands we append

#so in this case if it honda(as a carcompany) it would have models they would habve produce .... like a honda civic as a carmodel that honda produces 
civic= CarModel('civic')
accord = CarModel('accord')

honda = CarCompany('honda')

honda.car_brands_produced(civic)
# now pass cicic cause its the variable that holds the instance of our carmodel civic... 

honda.car_brands_produced(accord)


print([  m for m in honda.carmodel])
#when it comes to addd functionality to our coe we start asking a question whose responsibility is it to enact this behaviour
# like if we wanted to check how many instances a class has created who would we ask the instance ...... or the class that produces those instances 

# A class attribute is accessible to the entire class — it has class scope. A class method is a method that is called on the class itself, not on the instances of that class.
#What's important and what makes this a class attribute is where it is declared. A class attribute must be declared outside of any methods in the class.
# when a class is modifiedany objects

class Album:
    album_count = 0
    # this is a class level attribute/variable
    def __init__ (self , year):
        self.date = year

a1 = Album(1990)#
# when this instance was created the value count of album_count was 0 hence its count at the moment was 0
a1.album_count
# this will give zero

Album.album_count += 1
# here we've modified the album count to 1
#meaning that after the next instance will be created when the class variable is one
a2 = Album(2000)
a2.album_count
# this will give 1


# so if we warted to manipulate this we would .... put the adding code in our init ensuring that every time initialization occurs we add it to the class count
def __init__(self , year):
    Album.album_count +=1 

# the reason we do Album.album_count is since the album_count is found in our class scope .... while in init we are usually in the instance scope
# so if refering to change of the class scope we have to notate into the class then the variable hence
Album.album_count
#Using our class name and dot notation, we can access our class attributes anywhere in our class: in both class and instance methods.

# . This is a very useful feature, but what if we already have an album collection and want to manipulate the album_count attribute without creating new Album objects?
#we define a class method
@classmethod
def increment_album_count(cls):
    cls.album_count += 1
    

# Remember that methods are a type of function, and functions are first class objects in Python. Decorators allow us to use our new function as an argument and a return value to provide it some additional out-of-the-box functionality.
# CLS refers to the entire class itself not to an instace of the class
# So we use cls to refer to class attributes and methods within class methods. meaning that we are under class scope


#>>> class constants
# Class constants have a lot in common with class attributes. Both constants and attributes:

# Are defined in the body of the class.
# Can be accessed from within a class method.
# Can be accessed from within an instance method.
# When deciding when to use a class constant or a class attribute, the key distinction is that class constants are used to store data that doesn't change (is constant), while class attributes are used to store data that does change.

class  Band :
    INSTRUMENTS = ['Guitar' , 'Drums' , 'Jazz' ]
    player_count = 0

    def __init__ (self ,player):
        # if our instance being created has the constant ....
        if self.check_skill(player):
            self.player = player
            # low:
            self.increase_album_count()
            # lets think like this.... when im calling the first cls method in init ..... 
            # the value of genre being checked s the one being passed through initialization
            # ..... in the method ... it checks whether the parameter given is in the class constant
            # if it is it runs the if block ofcourse
    
    

        
    # for this guys to create the band we have to check if they have the skills required of the class to form at least one band instance ...
    # and this info is stored to the class right?? since we need all instances to follow that regime
    # You can call a class method from an instance, but it still operates on the class, not the instance.
    @classmethod
    #this means that this class method needs the parameter ......
    #cls says thats itworks on this class and its attributes and methods
    # self works on the instances ... but from instances .... we can still call the class methods in init
    def check_skill(cls,x):
        x in cls.INSTRUMENTS
    @classmethod
    def add_player(cls, increment = 1):
        cls.player_count = increment

    


    
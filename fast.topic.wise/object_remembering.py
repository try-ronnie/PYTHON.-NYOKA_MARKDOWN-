# Using Class Variables to Store Instances of a Class

class Song:
    all = []
    def __init__(self, name):
        self.name = name
        Song.add_list(self)
        # i would love to say that this realtes to the instance meaning
        # the reason we use self is that we are refering to the full object not its attribute 
    @classmethod
    def add_list (cls , x ):
        cls.all.append(x)
        

big_energy = Song("Big Energy")

# but if our user wanted to browse the songs they played python doesnt save the instances ...
#  So, how can we tell the Song class to keep track of every instance that it creates? We use a class attribute.

all =[]
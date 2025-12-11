
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
    # we involve a type check to ensure the value being passed must be an instance of author
    def author(self , value):
        if not isinstance(value , Author):
            raise TypeError('make sure Author is an instance of its class')
        else:
            self._author = value
    def all_books(self):
        #for all ites
        for items in Book.all:
            print(items.name , items .genre)
        
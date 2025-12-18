
class Author:
    all = []
    def __init__ (self , name):
        self.name = name
        # append this instance to get a memory list of all authors created
        Author.all.append(self)
    # if we would want to return all the books one author has created ...

    def author_books(self):
        return [for book in books if Book.all.author == self]
    



class Book :
    # this is to store the instances of book we generate
    all = []
    def __init__(self , name , genre):
        self.name = name
        self.genre = genre
        # since its not from this class and we will need to update it later we made it protected 
        # also remember for this to work 
        self._author = None
        Book.all.append(self)
    
    @property
    # getter method that returns the current value 
    # this also helps us get the value so we can update it accordingly
    def author(self):
        return self._author
    @author.setter
    # this primarily means that after creating the instance of book with the _author attribute set to none we shall need to change it
    # so we use the getter and setter method to ensure that we can 
    # we involve a type check to ensure the value being passed must be an instance of author

    def author(self , value):
        if not isinstance(value , Author):
            raise TypeError('make sure Author is an instance of its class')
        else:
            self._author = value
    def all_books(self):
        #for each instance  in our book_List
        #print the instances name and genre under the name items
        for items in Book.all:
            print(items.name , items .genre)
        
class Song:
    all = []
    count = 0  # cont of how many times instance has been created 
    genres = []
    artists= []
    genre_count = {} # this creates a histogram (shows quantitive data) how many times the 
    artist_count ={}
    

    def __init__(self, name  , artist , genre):
        self.artist = artist
        self.genre = genre
        self.name = name
        Song.add_song_to_count() 
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)

        # here we use the name of the class since it is the one that has the method and can use it


    @classmethod
    #this adds the value of count of songs ... meaning how many instances are created
    def add_song_to_count (cls , increment = 1):
        cls.count += increment
    # we use cls like to stick the method to the class 
    #cls tells the compiler that the method belongs to the class
    
    @classmethod
    def add_to_genres (cls , g_n):
        if g_n not in cls.genres:
            cls.genres.append(g_n)
        else:
            pass
    @classmethod
    def add_to_artists(cls, art):
        if art not in cls.artists:
            cls.artists.append(art)
        else:
            pass
    @classmethod
    def add_to_genre_count(cls, genre):
        # so to also maintain uniformity to ensure that the list also has what we are adding to the genre 
        cls.add_to_genres(genre)
        # if the genre is not in our list (that hold the none duplicates)
            #then create the value in the dict and assign it one
        #else if there is such a value it our list
            # then find the key and add +1 to its value

        if genre in cls.genres:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @ classmethod
    def add_to_artist_count(cls , artists0):
            # ensure that even when the histogram is updated the list to gets the same treatment
            cls.add_to_artists(artists0)
            if artists0  in cls.artists:
                cls.artist_count[artists0] += 1
            else:
                cls.artist_count[artists0] = 1
            
# remember that for a dict .... assigning something to a value and refering to it is just like appending in a list 



            

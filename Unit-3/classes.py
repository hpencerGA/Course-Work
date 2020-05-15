
#object orientated progamimg
#defining a class
#will use classes to create own data types
class Person: #blue print #typically class names are uppercase
    def __init__(self): # #every class will have init as a constructor and must accept self, two underscores, should always use self
        print('class instantiated')

    def dom_something(self):
        print('something done')

#p = Person()  #creates an object

#think of class as blue print to create an object

class Rectangle:   #four sided two long two short
    def __init__(self, l, w):  #length and width
        self.length = l
        self.width = w    #self.property creates a property
    
    def area(self):   #calculate area of rectangle
        return self.length * self.width
    
    #add method to calculate the perimeter
    def perimeter(self):
        return 2 * (self.length + self.width)

# need to create an object now
r1 = Rectangle(10, 5)

print(r1.area())

'''
def reverse_dict(input_dict):
    result = {}
    for key in input_dict:
        if type(input_dict[key]) is list or type(input_dict[key]) is dict:
            result[tuple(input_dict[key])] = key
        else:
            result[input_dict[key]] = key
    return result
'''


#playlist creating example
class Playlist:
    def __init__(self, name):
         #when playlist first create it is empty
         self.songs = []
         self.name = name    #line 37 and 38 define the class data items 

    #write the add_song method that will add a song to the playlist
    def add_song (self,song):  #when pass self python is keeping track of its data
        #validate the song data
        #has to have title, artist and length 
        #if has what we need append if not 
        #1. Check if the title appears
        #2. check then if the artist appears
        #3. check then if the length appears
        #if all appear go to next step
        #if not write not there
        #use type to check
        if type(song) is dict and 'title' in song and 'artist' in song and 'length' in song:
            self.songs.append(song)
        else:
            print('Invalid song format')
    
    #write get_titles method (return titles of playlist)
    #assume songs are dictionaries 
    #print the titles of songs in my playlist 
    def get_titles (self, title):
        titles = []  #cant be self.titles because not members of class
        for song in self.songs:
            titles.append(song['title'])
        
        return titles
    
    #write the duration method
    #return the total length of the playlist
    def total_length(self):
        total_length = 0
        for song in self.songs:
            total_length += song['length'] #dictionary name followed by key in square brackets
    
        return total_length

  


p = Playlist('my_travel_list')


p.add_song({
    'title': 'Bodak Yellow',
    'artist':'Cardi B',
    
})

p.add_song({
    'title': 'Shake it of',
    'artist': 'Taylor Swift',
    'length': 2.3

})        
    
p.add_song({
    'title': 'Through the Night',
    'artist': 'Travis Scott',
    'length': 4.15

})        


print(p.get_title())

    



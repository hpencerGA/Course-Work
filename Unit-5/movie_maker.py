#Inside this file define, a class called Movie The movie class should assign a title, genre, and running_time]
#1 when initialized. The movie class also has a cast variable, which is an empty list initially.


#2 Write an add_cast method to add an actor to the movie’s cast. Actor data sould be a dictionary that has
'''
the following data:
{
'name': 'Jane Doe'
'age': 31
'sex': 'F'
}
'''
#Your add_cast method should do a check that the data passed in is valid actor data. You should display an 
#error message if the data passed in doesn’t have all the required fields.

#write a method describe that prints the movie’s title, genre, running time and all its cast members

#Write a method called compare_to which compares one movie to another. This method accepts a movie
#object and compares it to the current movie object. If the two movies have less than two actors in common,
#the method must return -1, otherwise it returns 1.
#Write a method save_to_file that accepts a file name, and creates the file with the name given, and stores
#the movie date to the file. You should store the movie as a single dictionary. Use the json.dump method to
#save the data to the file.
#HINT: To store the data as a single dictionary, create a new dictionary with title, genre, running_time,
#and cast, as keys. The values will be your class data. You can them dump your newly created dictionary
#to file using json.dump



import json

class Movie:
    def __init__(self, title, genre, running_time):
        self.title = title
        self.genre = genre
        self.runing_time = running_time
        self.cast = []

    def add_cast(self,cast_member):
        if 'name' in cast_member and 'age' in cast_member and 'sex' in cast_member:
            self.cast.append(cast_member)
        else:
            raise ValueError('Error missing cast data')
    
    def describe(self):
        print(self.title, self.genre, self.runing_time, self.cast)
    
    def compare_to(self, other_movie):
        result = 0
        for cast_member in self.cast:
            if cast_member in other_movie.cast:
                result += 1

        if result >= 2:
            return 1
        else:
            return -1

#class solution
    def compare_to(self, other_movie):
        common_count = 0
        #return -1 if it has 1 or 0 actiors in common
        #otherwise return 1
        for item in self.cast:
            if item ['name']== other_item['name']:
                common_count += 1

        if common_count > 1:    
            return 1
    #no else because function ends at that return statement 
        return -1 

#when do m.variable access the class variable    
   
    def save_to_file(self,file_name):
        #have title, genre, running time and cast, you want to dump it all in a dict then a file
        dump_dict = {}
        dump_dict['title'] = self.title
        dump_dict['genre'] = self.genre
        dump_dict['running_time'] = self.running_time
        dump_dict['cast'] = self.cast

        with open(file_name, 'w') as dump_file:
            json.dump(dump_dict, dump_file)
        
    




#write to a file, need to open it
#w means write and will overwrite whatever we have in the file
#if want to add instead of overwrite use a different file mode called pen (a) however not on a seperate line 
#to make it on a new line do new line character \n
text_file = open('lines.txt','a')

text_file.write('\nHere is a fourth line')
text_file.close()

#make us of JSON
import json
#use with to read files because dont want to close each time we open a file
with open('orders.json','r') as input_file:
    order_list = json.load(input_file)
    #will take a file pointer and load it
print(order_list)


#Write a method save_to_file that accepts a file name, and creates the file with the name given, and stores
#the movie date to the file. You should store the movie as a single dictionary. Use the json.dump method to
#save the data to the file.
#HINT: To store the data as a single dictionary, create a new dictionary with title, genre, running_time,
#and cast, as keys. The values will be your class data. You can them dump your newly created dictionary
#to file using json.dump
        

#the_italian_job = Movie(title = "The Itlian Job")

#the_italian_job.add_cast(castmeber1)


#the_italian_job = Movie().__init__(title = "The Itlian Job")

#Terminator = Movie(title = "The Itlian Job ......")

#the_italian_job.compare(Terminator) =-1 
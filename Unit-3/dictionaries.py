#dictionary can be one line or multiple lines, it can be on multiply lines which is easier
#stores values of a  
#keys are unique in dictionary, cant have double keys defined
#keys have to be int, floats, strings- immutable (meaning cannot change it)
#lists cannot be a key in a dictionary because a list can change
#for key in: what is python looking at because there are pairs i.e name- harrison. however it is iterating over the keys of the dictonary
#seperate each dicatonary with a , should go {,}
#to read a dictionary more clearly use json so go import json at the top of code
#use print(json.dumps[cars, indent=2 #indententation level])
#when iterating over a loop need to think what are the items I am looking at:
#if have a list of strings example

#for each dicatonaries add price
import json

cars = [
    {
        'make': 'Toyota',
        'model': 'Camry',
        'year': '2017',
        'color': 'black'
    },
    {
        'make': 'Toyota',
        'model': 'Prius',
        'year': '205',
        'color': 'white'
    },
    {
        'make': 'Mercedes Benz',
        'model': 'A 250',
        'year': '2019',
        'color': 'grey'
    },
    {
        'make': 'Hyundai',
        'model': 'Elantra',
        'year': '2007',
        'color': 'grey'
    },
    {
        'make': 'Lexus',
        'model': 'IS 300',
        'year': '2020',
        'color': 'blue'
    },
]

#when have a list of dictionaries when do for in each thing is a dictionary

prices = [100,200,300,400,500]
'''
index = 0
for car in cars:
    #print the make of the car
    car['price'] = prices[index]
    index += 1
print(json.dumps(cars, indent =2))
'''
#class soluiton 2
for index, car in enumerate(cars): #enumerate takes a pair of index and item in the list and returns a pair of values 
    car['price'] = prices[index] #python look at index of structure and keeps track of the index for us. Can use to grab an index
'''
#my solution
for car in cars:
    if car ['make'] == 'Lexus':
        car['price'] = 1000

print(cars)
'''

#write a function called reverse_lookup
#accept a dictionary and a value and if no key then return a string no key match value
#return key that matches the value

#return key that matches the value
#if no match reutrn the string: 'No match for that value'

state_capitals = {
    "Alaska" : "Juneau"
,    
    "Colorado" : "Denver"
,
    "Oregon" : "Salem"
,
    "Texas" : "Austin"
}

def reverse_loopup(my_dictionary, value):
    for key in my_dictionary:
        if value == my_dictionary[key]:
            return key
    else:
        return('no match for that value')

print(reverse_loopup(state_capitals, 'Austin'))

#want to write a function called frequency_counter, accepts a string
#return a dicatonary with each word, and the number of times each word occurs in the string

#to take the words from the sentence and store in the dictionary
#key is going to be the word and value will be number of times word appears(the count)

def frequency_counter(sentence):
    result = {} #declare empty dictionary
    words = sentence.split()

    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    
    return result

print(frequency_counter('try this at is at free verse verse'))


 
    




'''
frequency_counter('here is a simple sentence')
{
    'here': 1,
    'is:': 1
    'a': 1
    'simple': 1
    'sentence': 1
}

frequency_counter(is this as it is)
result should 
'''

#dictionary additional info

stocks = {
   'AC': {'price': 14.55, 
   'volume': 1000000,
   },
   'spy': {'price': 248.19,
    'volume': 2000000
   },
    
} 

stocks['mmm'] = {'price': 10, 'volume': 500000 } #addto dict

print(stocks['mmm']['price'])



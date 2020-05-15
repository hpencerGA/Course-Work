'''
#Problem 1 Write a function called dict_merge that merges two dictionaries. If there are common keys, the merged
#dictionary should have a list of the values of the common keys
import json

def dict_merge(dict1,dict2):
    #merge dict 1 and dict 2
    #create a new dictionary that has key value pairs in dic 1 and dic2
    dict3 = {} #create a new dictionary
    for key in dict1:
        if key not in dict2: #'key is wrong because looking for the same key
            dict3[key] = dict1[key]
        else: #if key in dict 2
            dict3[key] = [dict2[key] , dict1[key]]
    for key in dict2:
        if key not in dict1:
            dict3[key] = dict2[key]
        else: #if key in dict 1
            dict3[key] = [dict2[key] , dict1[key]]
    return dict3 

print(dict_merge({'a': 1, 'b': 2}, {'c': 3, 'd': 4}))
print(dict_merge({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))
print(dict_merge({'x': 'one', 'y': 'two'}, {'x': 1.5, 'y': 3.7}))


    #1. key not in dict 2
    #2. key is not in dic 1
    #3. key is in both

#{'name: John', 'address': 'toronto', 'telephone': 000}

#Problem 2 #Write a function called list_to_dict that accepts a person list (which is a list of lists), and returns a 
#dictionary. Each list in the person list has only two items. The keys of your result dictionary should be the
#first item in each list, and the value should be the second item
#list_to_dict([['name', 'Alice'], ['job', 'Engineer'], ['city', 'Toronto']])

def list_to_dict(person_list):
    result = {}
    for item in person_list:
        result[item[0]] = item[1]
    
    return result
    
    
print(list_to_dict([ 'Alice'], ['job', 'Engineer'], ['city', 'Toronto'])


#1 take list 1- take name set as key then value as name
#2 go to list 2 take name set as key then value as job

#Write a function called reverse_dict to reverse a dictionary. This means, given a dictionary, return a new
#dictionary that has the keys of as values, and the values as keys

def reverse_dict(input_dict):
    result = {}
    for key in input_dict:
        if type(input_dict[key]) is list or type(input_dict[key]) is dict:
            result[tuple(inpute_dict[key])] = key
        else:
            result[input_dict[key]] = key
    return result
print(reverse_dict({'a': [1,2,3], 'b': [4,5,6], 'c':[7,8,9]}))
print(reverse_dict({'name': 'alicia', 'job':'Engineer', 'city': 'Toronto'}))
'''
playlist = [
    {
        'title': 'Bodak Yellow',
        'genre': 'Pop',
        'artiste': 'Cardi B',
        'year': '2017',
        'length': 3.25
    },
]

def all_titles(pl):
    for item in pl:
        print(item['title', ',',end=' '])

all_titles[playlist]
#expect playlist


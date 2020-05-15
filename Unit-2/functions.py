#to define a function = def function: this case beow add two numbers
'''
def add_two():
    result = 5 + 5

    print(result)
#nothing happens when you excute this code returns to the prompt
'''
#reason it is because need to tell python to call the function
'''
def add_two():
    result = 5 + 5
    print(result)

add_two() #to get result need to write this
'''
#need function to act as a helper do specefic task and it tells you about that task
#what if numbers are 3 and 4

#passing arguments to functions 
'''
def add_two(a, b):
    result = a + b
    print (result)

add_two (3, -4)
'''

#how basic functions work created to help us simplify code or write realted bits of code in a unit and use it over and over again

#when write function most time they return an answer we want
#this time use return result
'''
def add_two(a, b):
    result = a + b
    return result #when have return function it stops and returns the value

print(add_two(3, 10)) #issue is there is no display that it does not show
'''

#write a function that returns the sum of the integers in a list

def sum_list(a_list):
    result = 0
    for num in a_list:
        result += num
    return result

values = [1, 2, 3, 4, 5, 10, -15]
ans = sum_list(values)

print(ans)

  #list is like a placeholder, function expects input to get output


#write a function that reverses a string
'''
def rev_string(my_string): #rev string is the function name, you do not want to overwrite this code
    updated_string = '' #create an empty string

    index = len(my_string) - 1
    while index >= 0:
        updated_string += my_string[index]
        index -= 1
    
    return updated_string

print(rev_string('hello'))
'''
#reverse string take 2 using a for loop

def rev_using_for(any_string):
    result = ''
    for char in any_string:
        result = char + result #updating the result with char so wouldnt reverse it when switch char and result
    return result

print(rev_using_for('hello'))

#write a function that finds the intersection of two lists
#what does intersection mean? takes two lists and tell me the items in both lists


#return the items that are in both lists 1 and 2 in a new list

def intersect_list(list_1, list_2):
    result = []
    for item in list_1:
        if item in list_2:
            result.append(item)
    
    return result

print(intersect_list([1, 2, 3, 4, 'a'], [3, 'a', 'x']))
         
# dont want to change the data, the data that is passed in we are gonna use to createnew things

def my_func(my_data):







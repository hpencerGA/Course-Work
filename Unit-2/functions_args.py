#function that takes any number of parameters
#add any number of numbers
#arg is a parameter that pays as a function that we want to pass through arguments
#*arg specifies the number of arguments (can use a for loop to iterate over loop)
#use star to define the function

def multiply(*args):
    product = 1
    for num in args:
        product *= num
    
    return product


print(multiply(1))
print(multiply(1, 10))
print(multiply(5, -3, 7))
print(multiply(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

#keyword arguments, can specify false arugment with key words

def message(name, msg= 'Hello' ):
    print(msg + ' ' + name) #if had retunr then would need print message below instead of message


message('Harrison')
message('Princeton', msg='Hi how are you doing')

#function that allows any number of keyword arguments

l = ['a', 'b', 'c']

for item in l:
    print(item, end=' ')
print()


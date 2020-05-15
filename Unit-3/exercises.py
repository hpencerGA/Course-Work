#List comprehension

nums = [1, 3, 4, 6, 7, 11, -15, 28]

#create alist of only the evennumbers in nums
'''
even_nums = []
for num in nums:
    if num % 2 == 0:
        even_nums.append(num)

print(even_nums)
'''
#use a list comprehension
#even_nums = [num for num in nums if num % 2 == 0]
#print(even_nums)

#even_nums = [num for in nums if num % 2 ==0] 
#step 1 create a list , step 
# 2 write a for loop to iterate over, 
# 3 write result looking for before the for loop

vals = [2, 4, 6, 8]
#new list with square of vals

val_square = [val * val for val in vals]
print(val_square)

#create a new list with words longer than 4 characters #part 2 return the uppercase of the word
words = ['run', 'cat', 'hassle', 'print', 'class', 'pyth']

greater_four = [word.upper() for word in words if len(word) > 4 ] 
print(greater_four)

#dictionary comprehensions
person  = {'name': 'Alice', 'address': 'Toronto', 'occupation': 'Engineer'}
#looking at both keys and values, the item is the key 
new_person = { item: person [item] for item in person}
print (new_person)

#what if want to swap keys and values, swap in the start item with person and vis versa
new_person = { person [item]: item for item in person}
print (new_person)

#new function called.item (gets both key and value pairs (return the tuple))
new_person = { key:val for key, val in person.items()} #grabbing key and val seperate with comma, can also do .keys for just keys or .values for the values
print (new_person)

colors = {'red': 'Bold', 'green': 'lively', 'blue': 'calm', 'yellow': 'warm'}
#create a new dictionary with colors whos values are either warm or lively
new_colors = {color : colors[color] for color in colors if colors[color] == 'warm' or colors[color] == 'lively'}  
#how to get a key and value do name of dict [key this example is color]
#do key for first part this case its color 

print(new_colors)

#create new dictionary with the count of each letter in a string
word = 'Apple'
dict_count = {letter: word.count(letter) for letter in word}

print(dict_count)







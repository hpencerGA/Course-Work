#Truthy vs false, important to see what it evaluates to
#if you use or as long as one of the values is true then it will print it
#if one is false then entire expression is false

'''

if -1:
    print('this is true')
else:
    print('this is not true')

#Need if and an expression to evaluaete true or false

num = 5

if num > 10:
    print('num is greater than 10')
    print('this is good')
   ''' 

readings = [25, 18, -5, 11, -3, -15, 8, -18, 6, 13]

#count number of negative readings in the list
#have to do count variable outside the loop
'''
count = 0
for temp in readings:
    if temp < 0:
        count += 1 #adding 1 to the count

print(count)
        
#find the average of the postive readings 
'''
total = 0
count = 0
for temp in readings:
    if temp > 0:
        count += 1
        total += temp

print (total/count)

#Count how many titles has 'the' in it

count = 0
titles = ['The Avengers', 'Avengers age of Ultron','Captain America, The fist Avenger']
for title in titles:
    if 'The' in title:
        count +=1

print(f'list has {count} titles with "The"')


#How many vowels are in the string

string = 'There is a long string that has only a few vowels'
vowels = ['a','e','i','o','u']
count = 0

for char in string: 
    if char in vowels:
        count += 1

print(f'string has {count} vowels')












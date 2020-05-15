car_total = 13

#check if car total is even, : is the start of a block, whenever indentation it follows statement above.
# two == checks if something is equal 

if car_total % 2 == 0:
    print ('car total is even')
#this is the action if ^ if this is true, else function is for false
else:
    print ('car total is odd')

#possibility of four grades (range of grades) and have a letter correspond to it 80-100 A, 60-79 B, 50-59 c. less then 50 D

# elif with multiple conditions 

score = 45

if score >= 80:
    grade = 'A'
elif score >= 60:
    grade = 'B'
elif score >= 50:
    grade = 'c'
else:
    grade = 'D'

print (grade)

#fizzbuzz
#for the first 50 integers 
#if divisble by 3, print fizz
#if divisble by 5 print buzz
#if divisble by 15 print fizzbuss
#Num is range for 1-51
##my solution below

for num in range (1,51):
    if num % 15== 0:
        print ('fizzbuzz')
    elif num % 3 == 0:
        print ('Fizz')
    elif num % 5 == 0:
        print ('buzz')
    else:
        print (num)
'''
princeton solution below
whenever writing a block a code, basic if statement check if condition is true or false, thats why have a block,
ex if x === 10:
    this is one level of indentation and will be excuted if satasfied
elif will start another block, make sure finish statement with a colon:
order matters if first one is excuted will go to the end that why 15 should go first, because if 3 first 15 divvisble by 3 would print fizz, 3 and 5 dont matter as much


'''

# find the sum of even numbers between 1-10

total = 0
for num in range (1,11):
    if num % 2 == 0:
        #calculating a running sum because continsuloly being updated inside a loop, += update variable on the left
        total += num

print(total)


negative_num = [-1,-5,-2,-6,-3]
total = 0
for num in negative_num:
    if num % 2 == 0:
        total += num

print(total)
    







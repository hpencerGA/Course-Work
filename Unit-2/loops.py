#for loops is telling python to do something set times
#for num in range(1,11):

#control c to stop loop
#while loop is different can be excuted 0,1 or infinte times
#while loop starts when condition satsfied and keeps running
#to make sure it ends you need to modify the expression you are comparing on
num = 5

while num < 10:
    print ('yeah!')
    num += 1



#prompt the user to enter a number 
#if the number is equal to your secret, print you ae correct
#if not ask user to guess again and repeat
#any input into the keyboard is a string

secret = 7

user_val = int(input('Enter your guess: '))
while user_val!= secret:
    print('Nope, Guess again:')
    user_val = int(input('Enter your guess: '))

print('Correct')

#use in a while loop
#check if string is a palindrome same as forwards as backwards
'level', 'racecar', 'aaaa', 

string = 'level'
first = 0
last = -1
'''
while string [first] == string [last] and first <len(string):
    first += 1
    last+= -1
print (yes)

'''
new_string = ''
index = len(string) - 1

while index >= 0:
    new_string += string[index]
    index -= 1

#print(rev_string)

if new_string == string:
    print('level!!')
else: 
    print('no level')


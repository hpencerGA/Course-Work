#Given a string, replace every letter with its position in the alphabet
#How would we phrase this problem?
#look at each letter, replace with the corresponding postion in in the alphabet
#what is the input? The string
#what should the final result be?- should be a new string consiting of numbers
#how do you figure out where each letter falls in regards to numbering
#think alphabet has 26 letters, can create a list or can create a string

#think output should be something like below
'''
string_1 = 'abc'

result = '123'

string = 'level'

result = '1252312'
'''

string = 'Coronavirus'

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x','y', 'z']
#make new empty string 
new_string = ''

#look at each letter- need a loop to do this
#look at each character in string
#when using alphabet.index the index thinks a is 0 and z is 25

for char in string.lower():  #use .lower to conver string
    #check where in alphabet it falls. use index list method
    postion = alphabet.index(char) + 1

    #add the position to my new string
    new_string += str(postion)

#how to fix code to get correct postion since add +1
#If run all lower case code fine but if have mix need to make sure the string also works
#to solve this use .lower

print(new_string)
    










#Your program should count the number of strings in the list that have length greater than 3 and their first and last characters are the same.

odd_strings = ['abba', '111', 'canal', 'level', 'abc', 'racecar','123451' , '0.0', 'papa', '-pq-']
count = 0

for string in odd_strings:        
    if len(string) > 3 and string[0] == string[len(string)-1]:
        count += 1

print (count)

#can also use -1 is last character 


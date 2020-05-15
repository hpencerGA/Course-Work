#how to read a file in python
#what we need to do is tell python open the file
#if dont specefiy path it will think its your current path is correct
#r means read, w overwrite, a for append
text_file = open('lines.txt', 'r')

#how to view the contents of the file
lines = text_file.read()
text_file.close
print(lines)

#Make sure close the file at the end after reading it

#write to a file, need to open it
#w means write and will overwrite whatever we have in the file
#if want to add instead of overwrite use a different file mode called pen (a) however not on a seperate line 
#to make it on a new line do new line character \n
text_file = open('lines.txt','a')

text_file.write('\nHere is a fourth line')
text_file.close()

#make us of JSON
import json
#use with to read files because dont want to close each time we open a file
with open('orders.json','r') as input_file:
    order_list = json.load(input_file)
    #will take a file pointer and load it
print(order_list)


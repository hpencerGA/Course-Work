'''
numbers = [8,5,17]

#insert the number -5 at the front of the list
numbers.insert(0,-5)

#find the number of elements in the list
print (len(numbers))

# remove the last element in the list

last_el = numbers.pop()

print (last_el)
print (numbers)
print (len(numbers))

#print the second element in the list

print (numbers[1])
'''

grades = [70,85,91,21,60,45,90,56,77,88]

#add 5 to each grade in the list 
#we have to access each element(position) in the list, change the element 
#we need to access to the index, we can use range
 
for index in range (len(grades)):
    grades[index] += 5

print(grades)

#make each word past tense in the list

verbs = ['like', 'hate', 'fake', 'rake']

for index in range (len(verbs)):
    verbs[index] += 'd'

#how to put a letter before the first letter not the last
for index in range (len(verbs)):
    verbs[index] = 'd' + verbs[index]

print(verbs)

#pig game
#r is for roll and h is for hold


import random
score_to_win = 20
player1_score = 0
player2_score = 0
current_player = 1

# if player 1's turn:
if current_player == 1:
    #roll the dice
    die = random.randint(1, 6)
    print(f"player 1 rolled a {die}")

#if player 1 rolled a 1 reset the score and pass the turn
if die == 1:
    current_player = 2
    player1_score = 0
    print('It is now Player 2s turn')

#otherwise add the die score to player 1 score
else:
    player1_score += die
#\n is a new line
print("fplayer 1s score: {player1_score}", f"player 2s score: {player2_score, sep="\n) 

#check for win if 
if player1_score >= score_to_win:
    print('Player 1 win!')
    current_player = 0

#if current player 2 turn
elif current_player == 2:
    #roll the dice
    die = random.randint(1, 6)
    print(f'player 2 rolled a {die}')

#if player 2 rolled a 1 reset the score and pass the turn
if die == 1:
    current_player = 2
    player2_score = 0
#otherwise add the die score to player 1 score
else:
    player2_score += die

print("fplayer 2s score: {player2_score}", f"player 1s score: {player1_score, sep="\n)

#check for win if 
if player2_score >= score_to_win:
    print('Player 2 win!')
    current_player = 0


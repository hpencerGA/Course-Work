'''
import random

my_list = ['apple', 'hangman', 'python'] #apple is postion 0 , hangman 1, python is 2

index = random.randint(0, len(my_list)-1)

word = my_list[index]
count = 0

for char in word:
    print('_', end = ' ')
print()

while count < 6:
    guess = input('Enter your guess')
    if guess in word:
        print('Correct!', end  )
    else:
        count +=1
        print('Guess again', end = guess)
    
    print()
'''
#correct solution
import random
list_of_words = ["south", "ocean", "water", "canada", "virus"]
max_number_of_guesses = 5
def HangmangameSol2():
    current_number_of_guesses = 0
    current_word = random.choice(list_of_words)
    guessed_letters = []
    for index in range(len(current_word)):
        guessed_letters.append ("_")
    while current_number_of_guesses < max_number_of_guesses:
        print (guessed_letters)
        guess = input ("What is your guess ")
        if guess in current_word:
            for index in range (len(current_word)):
                if current_word[index] == guess:
                     guessed_letters [index] = guess
        else:
            current_number_of_guesses += 1 
            print (f"You have {max_number_of_guesses - current_number_of_guesses} guesses left, try again")
        if "_" not in guessed_letters:
            print ("You win!")
            break
    if current_number_of_guesses == max_number_of_guesses:
        print (f"You lose!, the word was {current_word}")
HangmangameSol2()









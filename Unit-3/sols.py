#problem 5 Write a function called possible_words that accespts a list of words and a list of characters, and returns
# the valid words that can be made from the characters given.
#NOTE: Repetition of characters is not allowed
#legal_words = ['go', 'bat' 'me', 'eat', 'goal', 'boy', 'run']
#letters = ['e', 'o', 'b', 'a', 'm', 'g', 'l']
#possible_words(legal_words, letters) # should return ['go', 'me', goal']
'''
def letter_count(word):
    count = {}
    for l in word:
        count[l]= count.get(l,0) + 1 #count.get retrives a value with a specific key
    
    return count

def possible_words(word_list, char_list):
    #which word in word list can be formed from the
    #characters in char list

    #iterate over word_list (each word be formed from chacters we have)
    for word in word_list:
        is_word_valid = True #default with true that word is valid 
        #check each character in the word
        valid_words = []
        char_count = letter_count(word)

        # cheack each character in the word
        for letter in word:
            if letter not in char_list:
                is_word_valid = False
            else:
                if char_list.count(letter) != char_count[letter]:   #.count is a list character count function
                    is_word_valid = False
            #now need to add valid word to list
        if is_word_valid:
            valid_words.append(word)
    return valid_words

legal_words = ['go', 'bat', 'me', 'eat', 'goal', 'boy', 'run']
letters = ['e', 'o', 'b', 'a', 'm', 'g', 'l']

print(possible_words(legal_words, letters))
'''

#Princetons code
def letter_count(word):
    count = {}
    for l in word:
        count[l] = count.get(l, 0) + 1
    return count


def possible_words(word_list, char_list):
    #which words in word_list can be formed from the 
    #charaters in char_list
    valid_words = []
    #iterate over word_list
    for word in word_list:
        is_word_valid = True
        #get a count of each character in word
        char_count = letter_count(word)
        #check each character in the word
        for letter in word:
            if letter not in char_list:
                is_word_valid = False
            else:
                if char_list.count(letter) != char_count[letter]:
                    is_word_valid = False
        #add valid word to a list
        if is_word_valid:
            valid_words.append(word)
    return valid_words
legal_words = ['go', 'bat', 'me', 'eat', 'goal', 'boy', 'run']
letters = ['e', 'o', 'b', 'a', 'm', 'g', 'l']


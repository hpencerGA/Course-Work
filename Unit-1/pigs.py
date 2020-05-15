import random
score_to_win = 20
player1_score = 0
player2_score = 0
current_player = 1
while True:
    #if player 1's turn:
    if current_player == 1:
        #roll the die
        die = random.randint(1, 6)
        print(f"Player 1 rolled a {die}")
        #if player 1 rolled a 1, reset the score and pass the turn
        if die == 1:
            current_player = 2
            player1_score = 0
            print("It is now Player 2's turn")
        
        #otherwise, add the die score to player 1's score
        else:
            player1_score += die
        
        print(f"Player 1's score: {player1_score}", f"Player 2's score: {player2_score}", sep="\n")
        #check for win
    #    if player1_score >= score_to_win:
    #        print("Player 1 wins!")
    #        current_player = 0
    #if player 2's turn
    elif current_player == 2:
        #roll the die
        die = random.randint(1, 6)
        print(f"Player 2 rolled a {die}")
        #if player 2 rolled a 1, reset the score and pass the turn
        if die == 1:
            current_player = 1
            player2_score = 0
            print("It is now Player 1's turn")
        #otherwise, add the die score to player 2's score
        else:
            player2_score += die
        print(f"Player 1's score: {player1_score}", f"Player 2's score: {player2_score}", sep="\n")
    #check for win
    if player2_score >= score_to_win or player1_score >= score_to_win:
        break
#print winner
if player1_score >= score_to_win:
    print("Player 1 wins!")
elif player2_score >= score_to_win:
    print("Player 2 wins!")
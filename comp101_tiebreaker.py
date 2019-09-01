# Made by: Leonardo Linardi (April 2017)

def comp101_tiebreaker(points, server):
    """ Takes a sequence of 'points' with each point represented by an integer
        0 or 1, indicating each 'point' is won by either Player 0 or Player 1,
        respectively. With the 'points' displayed in respective to the 
        serving player 'server'. 
        The winner of the game is determined when a player wins at least 
        7 points and also has 2 points more than the opponent.
        Returns the current score, the winner, and the points left 
        after the game. """
    
    player0_score = 0  # initial score of both players
    player1_score = 0
    remainder = []     # stores the remaining points if the game has ended
    winner = None      # initial winner of the game
    
    # tests every 'points' in 'points'
    for number in points:
        
        # finds the 'score' difference between both players and make
        # sure it is a positive value
        score_diff = abs(player0_score - player1_score)
        
        # checks whether the game has already ended or not
        if (player0_score >= 7 or player1_score >= 7) \
        and score_diff >= 2:
            
            # determines which player is the 'winner'
            if player0_score > player1_score:
                winner = 0
                
            else:
                winner = 1
            remainder.append(number)
                
        else:
            
            # accumulates the 'points' won by each player
            if number == 0:    
                    player0_score += 1
            else:
                player1_score += 1
                
    # updates the latest score difference
    score_diff = abs(player0_score - player1_score)

    # checks whether a player 'won' the game at exactly his 7th 'point'
    if (player0_score == 7 or player1_score == 7) \
    and score_diff >= 2:       
        
        # determines which player is the winner
        if player0_score > player1_score:
            winner = 0
        else:
            winner = 1
            
    # determines which player score is displayed first based on 'server'
    if server == 0:
        score = str(player0_score) + "-" + str(player1_score)
    else:
        score = str(player1_score) + "-" + str(player0_score)
    
    return (score, winner, remainder)
# Made by: Leonardo Linardi (April 2017)

def comp101_score(points, player):
    """ Takes a sequence of 'points', with each 'point' represented by an 
        integer 0 or 1, indicating each 'point' is won by either Player 0 or 
        Player 1, respectively. With the 'points' displayed in respective
        to the 'player' mentioned. Returns a tuple of scores won by each 
        player, with 'player's' score printed first. """
    
    player0_score = 0    # initial score of both players
    player1_score = 0
    
    # checks every integer in 'points' if it is won by 'player' 1 or 2
    for numbers in points:
        
        # accumulates the number of 'points' won by each player
        if numbers == 0:
            player0_score += 1
            
        else:
            player1_score += 1
    
    # checks which player's point should be displayed as 'score1' or first
    if player == 0:
        score1 = player0_score
        score2 = player1_score
        
    else:
        score1 = player1_score
        score2 = player0_score
        
    return (score1, score2)
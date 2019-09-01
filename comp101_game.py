# Made by: Leonardo Linardi (April 2017)

def comp101_game(points, server):
    """ Takes a sequence of 'points' with each point represented by an integer
        0 or 1, indicating each 'point' is won by either Player 0 or Player 1,
        respectively. With the 'scores' displayed in respective to the 
        serving player 'server'. 
        The 'winner' of the game is determined when a player wins at least 
        4 points in total and also has 2 points more than the opponent. 
        Returns the current score, the winner, and the points left 
        after the game. And returns an 'Ad' or "advantage" when both
        players scored at least 3 points, and one player has 1 more point
        than the other. """
    
    player0_points = 0 # sets initial 'points' of both players
    player1_points = 0 
    final0_score = 0   # final 'score' of both players in a manner peculiar to
    final1_score = 0   # tennis
    remainder = []     # stores the remaining 'points' if the game has ended
    tennis_score = {0: 0, 1: 15, 2: 30, 3: 40, 4: 40}   # use to convert
                                                        # 'points' to tennis
                                                        # 'scores'
    winner = None      # initial winner of the game
    
    # tests every 'points' in 'points'
    for number in points:
        
        # finds the 'point' differences between both players and make
        # sure it is a positive value
        points_diff = abs(player0_points - player1_points)
        
        if (player0_points >= 4 or player1_points >= 4):
            
            # the case when a 'winner' is found and stores the 
            # remaining 'points'
            if points_diff >= 2:
                if player0_points > player1_points:
                    winner = 0
                    final0_score = "W"
             
                else:
                    winner = 1
                    final1_score = "W"
                remainder.append(number)
           
            # the case when there is no 'winner' yet    
            else:
                
                if number == 0:
                    player0_points += 1

                else:
                    player1_points += 1
                
                # updates the latest 'point' difference
                points_diff = abs(player0_points - player1_points)
                
                # ONLY runs if a player 'won' the game after exactly getting 
                # his next 'point'
                if points_diff >= 2:
                    
                    if player0_points > player1_points:
                        winner = 0
                        final0_score = "W"
                        
                    else:
                        winner = 1
                        final1_score = "W"
                
                # if one of the player gets an "advantage"
                elif points_diff == 1:
                
                    if player0_points > player1_points:
                        final0_score = "Ad"
                        final1_score = 40
                    else:
                        final0_score = 40
                        final1_score = "Ad"
                
                # if no players get an "advantage" or 'wins' the game
                else:
                    final0_score = 40
                    final1_score = 40
        
        else:
            
            # adds a 'point' to a 'player' and converts player 'points' to 
            # 'scores' in a manner peculiar to tennis
            if number == 0:
                player0_points += 1
                final0_score = tennis_score[player0_points]
                
            else:
                player1_points += 1
                final1_score = tennis_score[player1_points]
    
    # updates the latest score difference
    points_diff = abs(player0_points - player1_points)
    
    # checks if a player gets an "advantage" / 'wins' the game at exactly 
    # his 4th 'point'
    if (player0_points == 4 or player1_points == 4):
        
        # when a player 'won' the game
        if points_diff >= 2:
            
                if player0_points > player1_points:
                    winner = 0
                    final0_score = "W"
                else:
                    winner = 1
                    final1_score = "W"
        
        # when a player gets an "advantage"
        elif points_diff == 1:
            
            if player0_points > player1_points:
                final0_score = "Ad"
            else:
                final1_score = "Ad" 
    
    # determines which player score is displayed first based on 'server'
    if server == 0:
        score = str(final0_score) + "-" + str(final1_score)
    else:
        score = str(final1_score) + "-" + str(final0_score)
    
    return (score, winner, remainder)                  
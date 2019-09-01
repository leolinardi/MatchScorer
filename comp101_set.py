# Made by: Leonardo Linardi (April 2017)

def comp101_set(points, server, tiebreaker=comp101_tiebreaker, 
                game=comp101_game):
    """ Takes a sequence of 'points' with each point represented by an integer
        0 or 1, indicating each 'point' is won by either Player 0 or Player 1,
        respectively. With the game 'score' displayed in respective to the 
        serving player 'server'. 
        The 'winner' of the 'match' is determined when a 'player' wins 6 games 
        and at least 2 games more than the 'opponent'. If the final match score 
        of the game is 6-6, a 'tiebreaker' game is played, to give a final
        score and decide which player is the 'winner'.
        Returns the current 'game' score, the winner, and the points left 
        in the match after the current set. """
    
    player0_game = 0      # sets the initial 'games' score won by both players
    player1_game = 0
    points_list = []      # stores all of the 'points' in the whole 'match'
    winner = None         # initial winner of the game
    
    # test every 'points' in 'points'
    for number in points:
        
        # store every 'points' inside a temporary list to be used in 'game'
        # and 'tiebreaker'
        points_list.append(number)
        
        # adds a 'score' for every 'game' won by a player and make sure 
        # it doesn't add another 'score' if the 'match' has been won/tied
        if not (player0_game >= 6 and player1_game >= 6) \
        and winner == None:
                
            if (game(points_list, server))[1] == 0:
                player0_game += 1
                
                # resets the current 'points' stored after a 'game' has been
                # completed
                del points_list[:]
                
            elif (game(points_list, server))[1] == 1:
                player1_game += 1
                del points_list[:]
                
        # finds the 'game' score differences between both players and make
        # sure it is a positive value
        game_diff = abs(player0_game - player1_game)
        
        if (player0_game >= 6 or player1_game >= 6):
            
            # runs when a winner is found
            if game_diff >= 2:
                if player0_game > player1_game:
                    winner = 0
                else:
                    winner = 1
            
            # runs when the 'match' is tied at 6-6
            if game_diff == 0:
                
                # stores the 'winner' and the 'points' remaining after the
                # the match has ended (when a winner is found)
                tie_winner = (tiebreaker(points_list, server))[1]
                tie_remainder = (tiebreaker(points_list, server))[2]
               
                if tie_winner == 0:
                    player0_game += 1
                    winner = 0
                    del points_list[:]
                    
                elif tie_winner == 1:
                    player1_game += 1
                    winner = 1
                    del points_list[:]     

    # updates the latest 'game' score differences
    game_diff = abs(player0_game - player1_game)
    
    # decides the source of the remaining 'points' that will be displayed as
    # 'remainder' when the function is returned
    if (player0_game >= 6 or player1_game >= 6):
        
        # the case when a winner is found before the 'tiebreaker' game
        if game_diff >= 2:
            remainder = points_list
            
        # the case when the 'match' is tied
        elif game_diff == 0:
            remainder = tie_remainder

        # the case when a winner is found after the 'tiebreaker' game
        elif player0_game == 7 or player1_game == 7:
            remainder = points_list
    
    else:
        remainder = (game(points_list, server))[2]
    
    # determines which player score is displayed first based on 'server'
    if server == 0:
        score = str(player0_game) + "-" + str(player1_game)
    
    else:
        score = str(player1_game) + "-" + str(player0_game)
        
    return(score, winner, remainder)   
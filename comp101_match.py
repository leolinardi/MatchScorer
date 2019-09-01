# Made by: Leonardo Linardi (April 2017)

def comp101_match(points, server, maxlen, tiebreaker=comp101_tiebreaker,
                  game=comp101_game, set_score=comp101_set):
    """ Takes a sequence of 'points' with each point represented by an integer
        0 or 1, indicating each 'point' is won by either Player 0 or Player 1,
        respectively. With the 'scores' displayed in respective to the 
        serving player 'server'.
        While 'maxlen' indicates the maximum length of the match in terms of
        sets, as a 'maxlen' of 3 means a best-of-three-set match, which means
        a 'winner' is determined when a 'player' wins 2 sets in that match.
        Returns the current completed 'set' score, the current incomplete set's
        'game' score, and the current incomplete game's 'points'. """

    player0_set = 0     # sets the initial 'set' score for both players
    player1_set = 0     
    set_list = []       # stores all of the 'points' in a temporary list
                        # to be use in counting 'sets'    
    final_results = ""  # stores the current 'set', 'game' and 'points' score 
    
    # test every 'points' in 'points'
    for number in points:
        
        set_list.append(number)
        
        # the case when a player wins a 'set'
        if (set_score(set_list, server))[1] in (0, 1):
            
            # checks whether the final 'result' to be display already 
            # contains a score or not
            if final_results != "":
                final_results += " " + (set_score(set_list, server))[0]
            
            else:
                final_results += (set_score(set_list, server))[0]
            
            # adds a 'set' score to the winning player of the 'set'
            if (set_score(set_list, server))[1] == 0:
                player0_set += 1
        
            elif (set_score(set_list, server))[1] == 1:
                player1_set += 1
            
            # resets the current 'points' stored when a 'set' has been won
            del set_list[:]
    
    # checks if the sequence of 'points' provided represents a valid match/
    # not too many points relative to the indicated match length
    if (player0_set + player1_set) == maxlen and set_list != []:
        return False
    
    # adds the current 'game' score if a 'set' is not completed
    if (set_score(set_list, server))[0] != "0-0":
        
        if final_results != "":
            final_results += " " + (set_score(set_list, server))[0]
        
        else:
            final_results += (set_score(set_list, server))[0]
    
    points_list = []    # stores all of the 'points' in a temporary list
                        # to be use in counting 'sets' 
    player0_game = 0    # sets the initial 'game' score for both players
    player1_game = 0
    
    # finds the current 'game' score and determine where the 'points' will go
    # (to a normal game scoring/tiebreaker game)
    for number in set_list:    
        
        points_list.append(number)
        
        # adds a 'game' score to the winner of the 'game'
        if (game(points_list, server))[1] == 0:
            player0_game += 1
            del points_list[:]
            
        elif (game(points_list, server))[1] == 1:
            player1_game += 1
            del points_list[:]    
    
    # the case when a game is 'tied'
    if player0_game == 6 and player1_game == 6:
        game_points = (tiebreaker(points_list, server))[0]
        
    # the case when a game doesn't end in a 'tie'
    else:
        game_points = (game(points_list, server))[0]
    
    # adds the current 'point' score for the current incomplete 'game'
    if game_points != "0-0":
        
        if final_results != "":
            final_results += " " + game_points
        
        else:    
            final_results += game_points
    
    return(final_results)   
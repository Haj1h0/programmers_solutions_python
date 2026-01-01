def solution(players, callings):
    
    h1 = {player : i for i, player in enumerate(players)}
    h2 = {i : player for i, player in enumerate(players)}
        
    #   h1, h2 = {}, {}    
    #   for i, player in enumerate(players):
    #       h1[player] = i              
    #       h2[i] = player              
    
    # swap
    for calling in callings:        
        r = h1[calling]                 # 등수
        h1[h2[r-1]],h1[h2[r]] = h1[h2[r]],h1[h2[r-1]]
        h2[r-1],h2[r] = h2[r],h2[r-1]   # i -> player 등수에 따른 player 변화       
        
    #   bf = h2[h1[calling]-1]      # bf = h2[2] == "poe"
    #   h1[calling] -= 1            # h1["kai"] -= 1    
    #   h1[bf] += 1                 # h1["poe"] += 1
    #   h2[h1[calling]+1] = bf
    #   h2[h1[calling]] = calling
    
    return list(h2.values())

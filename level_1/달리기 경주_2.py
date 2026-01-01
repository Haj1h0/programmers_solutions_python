def solution(players, callings):
    pla_dic = {key: i for i, key in enumerate(players)}

    for p in callings:	                                      # 추월한 선수
        c = pla_dic[p]                                        # 추월한 선수의 원래 등수
        pla_dic[p] -= 1                                       # 추월한 선수의 추월 이후 등수로 업데이트
        pla_dic[players[c-1]] += 1                            # 추월한 선수 앞에 있던 선수 등수 하나 내리는 업데이트
        players[c-1], players[c] = players[c], players[c-1]   # player list swap

    return players

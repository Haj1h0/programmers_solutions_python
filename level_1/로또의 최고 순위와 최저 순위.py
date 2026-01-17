from collections import Counter

# lottos, win_nums : 길이가 6인 구매한 로또 번호, 길이가 6인 정답 로또 번호
def solution(lottos, win_nums):  
    
    # rank : 맞은 번호 당 로또 등수를 담고 있는 hash
    # l , w : hash를 씌운 lottos와 win_nums
    # win : 0 제외 구매한 로또 번호 중 맞은 로또 번호의 수
    rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    l, w = Counter(lottos), Counter(win_nums)
    win = sum((l & w).values())
    return [rank[win+l[0]], rank[win]]

def solution(cards1, cards2, goal):
    for i in goal:
        if cards1[:1] == [i]:
            del cards1[0]          # cards1.pop(0)
        elif cards2[:1] == [i]:
            del cards2[0]
        else:
            return "No"
    return "Yes"

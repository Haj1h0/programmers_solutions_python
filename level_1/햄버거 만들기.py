def solution(ingredient):
    h, result = [], 0
    for i in ingredient:
        h.append(i)    
        if len(h) >= 4 and i == 1:
            if h[-2] == 3 and h[-3] == 2 and h[-4] == 1:     # len() -> O(1)
                del h[-4:]
                result += 1
    return result

def digit_reverse(n):
    return list(map(int, reversed(str(n))))

def solution(n):
    a = list(str(n))    
    a.reverse()
    return [int(i) for i in a]

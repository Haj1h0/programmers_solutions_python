def solution(n):
    n3 = []
    while n:
        n3.append(n % 3)
        n = n // 3      
    return sum([j * 3**i for i, j in enumerate(reversed(n3))])

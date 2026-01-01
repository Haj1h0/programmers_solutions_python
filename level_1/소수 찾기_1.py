import math

def solution(n):
    ans = 0
    for i in range(1, n+1):
        ans += p(i)         
    return ans

def p(n):
    if math.sqrt(n) % 1 == 0:
        return 0
    elif math.sqrt(n) % 1 != 0:
        for i in range(1, int(math.sqrt(n)) + 1):
            if i != 1 and n % i == 0:
                return 0
    return 1

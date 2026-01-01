def solution(n, m):
    nl = [i for i in range(1, n // 2 + 1) if n % i == 0] + [n]
    ml = [i for i in range(1, m // 2 + 1) if m % i == 0] + [m]
    
    x = 0
    for i in nl:
        for j in ml:
            if (i * j) % n == 0 and (i * j) % m == 0: 
                x = i * j
                break
        if x > 0:
            break
            
    answer = [max([i for i in nl if i in ml]), x]
    return answer


"""
def solution(n, m):
    gcd = lambda a, b : b if not a % b else gcd(b, a % b)
    lcm = lambda a, b : a * b // gcd(a, b)
    return [gcd(n, m), lcm(n, m)]
"""

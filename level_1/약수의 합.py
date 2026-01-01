def solution(n):
    return sum([i for i in range(1, n+1) if n % i == 0])

"""
def sumDivisor(num):
    # num / 2 의 수들만 검사
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])
"""

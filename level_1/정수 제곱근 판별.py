def solution(n):
    ans = ((n ** 0.5) + 1) ** 2 if (n ** 0.5) % 1 == 0 else -1
    return ans

def solution(d, budget):
    answer = 0
    for i, v in enumerate(sorted(d), start = 1):
        if answer + v <= budget:
            answer += v
        elif answer + v > budget:
            return i - 1
    return len(d)

"""
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)
"""

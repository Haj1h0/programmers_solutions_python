def solution(n):
    answer = ['수' if i % 2 != 0 else '박' for i in range(1, n + 1)]
    return ''.join(answer)

"""
def water_melon(n):
    return "수박" * (n//2) + "수" * (n%2)
    # 문자열에 곱 연산
"""

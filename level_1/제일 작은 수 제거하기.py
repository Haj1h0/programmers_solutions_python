def solution(arr):
    n = min(arr)
    return [i for i in arr if i != n] or [-1]

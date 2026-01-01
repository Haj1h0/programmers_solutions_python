def solution(n, arr1, arr2):
    arr1 = list(map(lambda x : ('0'*n + bin(x)[2:])[-n:], arr1))
    arr2 = list(map(lambda x : ('0'*n + bin(x)[2:])[-n:], arr2))
    return ["".join('#' if int(i) or int(j) else ' ' for i , j in zip(*ar)) for ar in zip(arr1, arr2)]

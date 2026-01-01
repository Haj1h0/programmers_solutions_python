def solution(t, p):
    l, cnt = len(p), 0
    for i in range(len(t)):
        if i + l <= len(t) and int(t[i : i + l]) <= int(p):
            cnt += 1
    return cnt

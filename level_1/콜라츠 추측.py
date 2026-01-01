def solution(num):
    cnt = 0
    while cnt != 500:
        cnt += 1
        if cnt == 1 and num == 1:
            return 0
        if num % 2 == 0:
            num = num / 2
        elif num % 2 != 0:
            num = num * 3 + 1
        if num == 1:
            return cnt
    return -1

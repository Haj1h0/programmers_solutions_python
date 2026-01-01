def solution(number):
    cnt = 0
    for i, num1 in enumerate(number):
        for j, num2 in enumerate(number[i + 1:], start = i + 1):
            for num3 in enumerate(number[j + 1:]):
                if num1 + num2 + num3 == 0:
                    cnt += 1

    return cnt

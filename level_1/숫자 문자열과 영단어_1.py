def solution(s):
    num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    alp = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    h = {alp[int(i)] : i for i in num}
    p, answer = "", ""
    for i in s:
        p += i
        if p in num:
            answer += p
            p = ""
        elif p in alp:
            answer += h[p]
            p = ""

    return int(answer)

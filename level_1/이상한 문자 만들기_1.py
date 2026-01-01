def solution(s):
    ans = []
    for word in s.split(" "):
        answer = ""
        for i, w in enumerate(word, start = 1):
            if i % 2 != 0:
                answer += w.upper()
            else:    
                answer += w.lower()
        ans.append(answer)                

    return " ".join(ans)

    # s.split(" ")
    # ['try', 'hello', 'world']

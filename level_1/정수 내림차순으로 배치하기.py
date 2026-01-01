def solution(n):
    return int("".join(sorted(str(n), reverse= True)))
    
# a = "52312"
# print(sorted(a))
# ['1', '2', '2', '3', '5']

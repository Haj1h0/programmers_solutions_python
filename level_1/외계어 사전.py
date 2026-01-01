def solution(spell, dic):
    return min(([1 if set(spell) == set(d) else 2 for d in dic]))  

"""
spell = set(spell)    
answer = 2
for d in dic:
    if spell == set(d):
        answer = 1
        break
"""

def solution(string):
    answer, bp = 0, []
    for i, s in enumerate(string):
        if not bp:                                # empty list
            bp.append(s)
            if i == len(string) - 1:
                answer += 1
        elif bp:                                  # empty list return False
            if s == bp[0]:
                bp.append(s)                
            elif s != bp[0]:
                bp.pop()                
            if not bp or i == len(string) - 1:    # empty list
                answer += 1

    return answer

"""
lst1 = []
lst2 = [1]
if not lst1:  print("lst1 is empty")
if lst2:      print("lst2 is not empty")

>>>  lst1 is empty 
>>>  lst2 is not empty
"""

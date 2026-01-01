def solution(s):
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for i in s:
        if i not in num:
            return False
      
#     if not (len(s) == 4 or len(s) == 6):
#         return False
    
#     return True

    if len(s) == 4 or len(s) == 6:
        return True
    
    return False

def sumMatrix(A,B):
    return [list(map(sum, zip(*x))) for x in zip(A, B)]
    
"""
for x in zip(A, B):
    print(x)
>>> ([1, 2], [3, 4]) 
튜플 unpacking후 zip으로 묶어주기
"""

def solution(x):    
    ans = True if x % sum(map(int,str(x))) == 0 else False
    return ans    

# ans = True if x % sum(list(map(int,str(x)))) == 0 else False
# map object도 iterable한 객체라서 list 선언하지 않아도 된다.
# return x % sum(map(int,str(x))) == 0

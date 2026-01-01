def solution(price, money, count):
    cnt = 0
    for i in range(1,count+1):
        cnt += i
        
    if money - price * cnt >= 0:
        return 0
    else:
        return price * cnt - money

"""
def solution(price, money, count):
    return abs(min(money - sum([price*i for i in range(1,count+1)]),0))
"""

def solution(participant, completion):
    
    answer = ''
    chk = {}
    
    for name in participant:
        chk[name] = chk[name] + 1 if name in chk else 1
        
    # if name in chk:
    #     chk[name] += 1
    # elif name not in chk:
    #     chk[name] = 1
        
    # chk[name] = chk.get(name, 0) + 1
    # dict.get(key, defualt = None)		key에 해당하는 value가져오고 없으면 return 0
              
    
    for name in completion:
        chk[name] -= 1
        
    # for name in chk:
    #     if chk[name] == 1:
    #         answer = name
    #         break
    
            
    for key, val in chk.items():
        if val == 1:     answer = key
        
    # dnf = [k for k, v in chk.items() if v > 0]	answer = dnf[0]    
    
    return answer

    # dic을 for문을 통해 돌리면 key값이 할당된다.
    # value값 접근 위해서는 .values()를 사용한다.
    # key와 value값을 동시에 접근하기 위해서는 items()를 사용한다.
    # dictionary는 원소들을 해시를 이용해 O(1) 상수 시간에 접근 가능하기에
    # 해당 코드는 O(n)의 시간 복잡도를 가진다.

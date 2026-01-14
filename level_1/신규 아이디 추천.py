def solution(new_id):
    int_num = "1234567890"
    ord_num = [i for i in range(97, 123)]
    
    # step 1
    new_id = new_id.lower()  
    
    # step 2
    new_id = ''.join([i for i in new_id if ord(i) in ord_num or i == "-" or i == "_" or i == "." or i in int_num])
    
    # step 3
    def dots(s: str):
        res = []
        prev = None

        for ch in s:  # 현재 문자 기준
            if ch == '.' and prev == '.':   
                continue
            res.append(ch)
            prev = ch

        return ''.join(res)
      
    new_id = dots(new_id) 
    
    # step 4
    new_id = new_id.strip('.')

    # step 5
    if not new_id:  new_id += 'a'
    
    # step 6
    if len(new_id) >= 16:       
        new_id = new_id[:15]
        if new_id[-1] == '.':  
            new_id = new_id[:-1]
        
    # step 7
    while(len(new_id) <= 2):
        new_id += new_id[-1]
    
    return new_id

    # “버릴 조건을 위에 계속 쌓아가는 구조”  
    # if A: continue
    # if B: continue
    # if C: continue
    # append

    # step 2
    # allowed = set("abcdefghijklmnopqrstuvwxyz0123456789-_.")
    # new_id = ''.join(ch for ch in new_id if ch in allowed)
  
    # step3
    # bf = new_id[0]
    # new_id_str = []
    # for i in new_id[1:]:
    #     if not (bf == i and i == "."):
    #         new_id_str.append(bf)
    #     bf = i
    # if not (new_id_str[-1:] == "." and new_id[-1:] == "."): # 빈값이면 에러 발생
    #     new_id_str.append(new_id[-1])  

def solution(n, m, section):

    sec = set(i for i in section)
    answer = 0    
  
    for i in section:
        if i in sec:
            bf = set(range(i, i + m))
            sec -= bf
            answer += 1 
          
    return answer

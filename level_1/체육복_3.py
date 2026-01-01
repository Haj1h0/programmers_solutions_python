def solution(n, lost, reserve):
	
    # 체육복을 도난당했지만 여분이 있어 빌릴 필요가 없는 집합
    s = set(lost) & set(reserve)	
    
    # 체육복을 빌려야 하는 집합
    l = set(lost) - s
    
    # 체육복을 빌려줄 수 있는 집합
    r = set(reserve) - s			
    
    for x in sorted(r):				# 체육복을 빌려줄 수 있는 크기(번호) 순으로 정렬 
    	if x - 1 in l:
        	l.remove(x - 1)
        elif x + 1 in l:
        	l.remove(x + 1)
       
    return n - len(l)
    
# set(r)의 원소 수를 k라 하면 전체 알고리즘의 복잡도는 O(klogK)

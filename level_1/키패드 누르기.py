def solution(numbers, hand):
  
    answer, l, r = '', '*', '#'
    push = {1 : 'L', 4 : 'L', 7 : 'L', 3 : 'R', 6 : 'R', 9 : 'R', 2 : 'F', 5 : 'F', 8 : 'F', 0 : 'F'}   # 2,5,8,0 은 'F'
    f = {1 : [0,0], 2 : [0,1], 3 : [0,2], 4 : [1,0], 5 : [1,1], 6 : [1,2], 7 : [2,0], 8 : [2,1], 9 : [2,2], '*' : [3,0], 0 : [3,1], '#' : [3,2]}
    h = ['L' if hand == "left" else 'R'] 
  
    for num in numbers:
        if push[num] == 'L':
            l = num
            answer += push[num]
        elif push[num] == 'R':
            r = num
            answer += push[num]
        else: # 2, 5, 8, 0
            lf = abs(f[num][0]-f[l][0]) + abs(f[num][1]-f[l][1])
            rf = abs(f[num][0]-f[r][0]) + abs(f[num][1]-f[r][1])
            if lf > rf: # 왼손이 더 먼 경우
                r = num
                answer += 'R'
            elif lf < rf: # 오른손이 더 먼 경우
                l = num
                answer += 'L'
            elif lf == rf: # 거리가 같은 경우
                answer += h[0]
                if h[0] == 'L':
                    l = num
                elif h[0] == 'R':
                    r = num
    return answer

"""
눌러야 할 숫자 : 1, 4, 7 인 경우는 무조건 L
눌러야 할 숫자 : 3, 6, 9 인 경우는 무조건 R
2, 5, 8, 0 인 경우에만 왼손과 오른손의 엄지손가락 위치에 따른 거리의 영향을 받는다.
그렇다면 해당 4개의 숫자를 눌러야 할 경우 무엇이 더 가까운지를 어떻게 비교할까?
case 1) 이차원 배열로 생각하여 index로 거리를 측정할 수 있게 로직을 짜보자
p = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
ex) 왼손 1, 오른손 6인 경우 8을 눌러야 한다. 1 = p[0][0], 6 = p[1][2], 8 = p[2][1] 을 확인하면 거리를 구할 수 있다. 
이를 dict로 만들어서 각 키패드 key값에 해당 좌표 value를 매칭시킨다.
또한 2, 5, 8, 0중 번호를 중복해서 누르는 케이스도 생각해야 한다.
"""

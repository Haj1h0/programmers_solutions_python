# number 문자열의 index 1번째 자리부터 시작하여
# 바라보는 숫자가 자신의 앞에 있는 숫자보다 클 경우에
# 자신의 앞에 있는 숫자를 지운다.
# 해당 과정이 진행되면 k = k -1 업데이트되며
# 숫자를 지운 새로운 number 문자열이 만들어진다.
# 위 과정을 업데이트되고 남은 k번 만큼 반복한다.
# number 문자열 끝까지 돌았지만 조건에 걸리지 않아 지워지는 숫자가 없는 경우
# number 문자열 맨 뒤에서 부터 k개 만큼 지운다.
# case 1) number = "98765", k = 2 일 경우 

def solution(number, k):
    number = list(number)
    if k == 0:
        return ''.join(number)
    elif k > 0:
        for index, i in enumerate(number[1:], start = 1):
            pre = number[index-1]  # 바라보는 숫자 앞에 있는 숫자
            if pre < i:
                number.pop(index-1)
                return solution(number, k-1)
            elif index + 1 == len(number):
                for i in range(k):
                    number.pop(-1)
                return ''.join(number)

# 합계: 58.3 / 100.0 시간초과, 런타임 에러
# number는 2자리 이상, 1,000,000자리 이하인 숫자입니다.
# 한 번 지울 때마다 pop(index-1) (중간 삭제라 O(n))
# 그리고 지운 뒤 solution(...)로 처음부터 다시 스캔 (또 O(n))
# 이걸 최대 k번 반복 → 최악 O(nk) ~ O(n²)
# k가 크면 재귀 깊이도 터질 수 있음
              
# “삭제는 중간을 흔든다 → 중간 pop은 비싸다”
# “삭제의 영향은 국소적이다 → 전체 재탐색은 낭비다”
# “국소적으로 되돌아가며 확인해야 한다 → 스택 / while이다”

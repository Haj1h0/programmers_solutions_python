def solution(numbers):
    result, answer = set(), []
    for i in range(len(numbers) - 1):
        for j in numbers[i + 1:]:
            result.add(numbers[i] + j)

    return sorted(list(result))

# set은 set생성자를 이용해 생성해야한다. 
# set(집합)의 원소 추가 = .add
# set(집합)의 update = .update
# set은 중복은 자동으로 제거되고 수정이라는 개념보다, 여러데이터를 한번에 추가할 때 사용합니다.
# k = {1, 2, 3}
# k.update([3, 4, 5])
# k
# {1, 2, 3, 4, 5}

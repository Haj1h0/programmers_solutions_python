def solution(participant, completion):
  participant.sort()
  completion.sort()
  for i in range(len(completion)):
    if participant[i] != completion[i]:
      return participant[i]
  return particiapnt[len(participant)-1]
    
# sort를 사용함으로서 0(NlonN)의 시간복잡도를 가진다.

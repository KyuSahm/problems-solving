'''
럭키 스트레이트
"이것이 코딩테스트다" p 321

입력1:
123402

출력1:
LUCKY

입력2:
7755

출력2:
READY
'''

if __name__ == '__main__':
  s = input()

  half = int(len(s) / 2)

  head_sum = 0
  for i in range(half):
    head_sum += int(s[i])

  tail_sum = 0
  for i in range(half, len(s)):
    tail_sum += int(s[i])

  if head_sum == tail_sum:
    print('LUCKY')
  else:
    print('READY')
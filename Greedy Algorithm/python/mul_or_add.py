'''
곱하기 혹은 더하기
"이것이 코딩테스트다" p 312

입력1:
02984

출력1:
576

입력2:
567

출력2:
210
'''

if __name__ == '__main__':
  s = input()

  ans = int(s[0])
  for i in range(1, len(s)):
    n = int(s[i])
    if ans <= 1 or n <= 1: 
      ans += n
    else:
      ans *= n

  print(ans)
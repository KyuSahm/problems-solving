'''
모험가 길드
"이것이 코딩테스트다" p 311

입력:
5
2 3 1 2 2

출력:
2

입력:
6
2 3 1 2 2 2

출력:
3

입력:
6
2 2 2 2 2 3

출력:
2

입력:
5
1 2 2 2 5

출력:
2
'''
if __name__ == '__main__':
  n = int(input())
  a = list(map(int, input().split()))

  a.sort()

  count = 0
  target = 0
  ans = 0
  
  for i in range(len(a)):
    target = max(a[i], target)
    count += 1
    if count >= target:
      ans += 1
      target = 0
      count = 0

  print(ans)
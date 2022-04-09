'''
두 배열의 원소 교체
"이것이 코딩테스트다" page 182

예1)
입력:
5 3
1 2 5 4 3
5 5 6 6 5

출력:
26
'''
if __name__ == '__main__':
  n, k = map(int, input().split())

  a = list(map(int, input().split()))
  b = list(map(int, input().split()))

  a.sort()
  b.sort(reverse=True)

  for i in range(k):
    if b[i] > a[i]:
      a[i], b[i] = b[i], a[i]
    else:
      break  

  print(sum(a))
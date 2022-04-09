'''
효율적인 화폐구성
"이것이 코딩테스트다" p225

입력 1:
2 15
2
3

출력:
5

입력 2:
3 4
3
5
7

출력:
-1

입력 3:
4 22
2
3
5
7

출력:
4

입력 4:
3 7
2
3
5

출력:
2
'''
import time

def my_solution(n, m, c_types, ans):
  start = min(c_types)
  for i in range(start, m + 1):
    for c in c_types:
      # 두 배의 메모리를 할당하면 조건문을 제거 가능
      if i - c > 0:
        ans[i] = min(ans[i - c] + 1, ans[i])
    #print(i, ans[i])  
  
  if ans[m] >= INF:
    return -1
  else:
    return ans[m]

def book_solution(n, m, c_types, ans):
  for i in range(n):
    start = c_types[i]
    ans[start] = 1
    for j in range(start + 1, m + 1):
      ans[j] = min(ans[j], ans[j - start] + 1)
  
  if ans[m] >= INF:
    return -1
  else:
    return ans[m]


if __name__ == '__main__':
  INPUT_MAX_CNT = 10001
  INF = int(1e9)

  n, m = map(int, input().split())

  # 조건문을 제거하기 위해 2배의 메모리 할당 
  #ans = [INF] * (2 * INPUT_MAX_CNT) 
  ans = [INF] * INPUT_MAX_CNT 
  c_types = []
  for _ in range(n):
    c = int(input())
    c_types.append(c)
    ans[c] = 1
  
  s_time = time.time()
  answer = my_solution(n, m, c_types, ans)
  e_time = time.time()
  print("my solution- answer: {}, elapsed time: {}".format(answer, e_time - s_time))

  ans = [INF] * (INPUT_MAX_CNT + 1)
  s_time = time.time()
  answer = book_solution(n, m, c_types, ans)
  e_time = time.time()
  print("book solution- answer: {}, elapsed time: {}".format(answer, e_time - s_time))
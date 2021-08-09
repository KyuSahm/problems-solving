'''
플로이드 워셜 알고리즘 구현
이것이 코딩테스트다 p251

입력데이터:
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4 
4 3 2

답:
0 4 8 6 
3 0 7 9 
5 9 0 4 
7 11 2 0
'''

if __name__ == '__main__':
  INF = 1e9

  n = int(input())
  m = int(input())

  graph = [[int(INF)] * (n + 1) for _ in range(n + 1)]

  #print(graph)

  for i in range(1, n + 1):
    graph[i][i] = 0
 
  for _ in range(m):
    i, j, cost = map(int, input().split())
    graph[i][j] = cost
  
  for k in range(1, n + 1):
    for i in range(1, n + 1):
      if i == k:
        continue  
      for j in range(1, n + 1):
          if j == k:
            continue
          graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

  print("answer:")
  for i in range(1, n + 1):
      for j in range(1, n + 1):
          if graph[i][j] == INF:
            print("INF", end=' ')
          else:  
            print(graph[i][j], end=' ')
      print()

'''
경쟁적 전염
이것이 코딩 테스트다 p344

입력:
3 3
1 0 2
0 0 0
3 0 0
2 3 2

해답:
graph:
1 1 2 
1 1 2 
3 3 2 
answer: 3

입력:
3 3
1 0 2
0 0 0
3 0 0
1 2 2

해답:
graph:
1 1 2 
1 0 2 
3 3 0 
answer: 0

'''
import operator

from collections import deque

if __name__ == '__main__':
  n, k = map(int, input().split())

  INF = int(1e9)
  graph = [[INF] * (k + 1) for _ in range(n + 1)]
  for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(1, k + 1):
      graph[i][j] = row[j - 1]

  #print(graph)
  
  s, x, y = map(int, input().split())

  viruses = []

  for i in range (1, n + 1):
    for j in range (1, k + 1):
      if graph[i][j] != 0:
        # (sec, virus type, x, y)
        viruses.append((0, graph[i][j], i, j))

  viruses.sort(key=operator.itemgetter(0, 1))
  #print(viruses)

  q = deque(viruses)
  
  offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
  while q:
    cs, i, a, b = q.popleft()
    
    if cs >= s:
      break

    for dx, dy in offsets:
      new_a = a + dx
      new_b = b + dy
      if new_a >= 1 and new_a <= n and new_b >= 1 and new_b <= k:
        if graph[new_a][new_b] == 0:
          graph[new_a][new_b] = i
          q.append((cs + 1, i, new_a, new_b))

  print("graph:") 
  for i in range(1, n + 1):
    for j in range(1, k + 1):
      print(graph[i][j], end=' ')
    print()

  print("answer: {}".format(graph[x][y]))
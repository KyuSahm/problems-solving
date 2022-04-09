'''
특정 거리의 도시 찾기
"이것이 코딩 테스트다"의 page 339
'''
from collections import deque

if __name__ == '__main__':
  # n => number of city, m => number of path
  # k => distance between cities
  # x => start city number
  n, m, k, x = map(int, input().split())
  
  INF = 1e9
  graph = [[] for _ in range(n + 1)]
  distance = [INF] * (n + 1)

  for i in range(m):
    from_city, to_city = map(int, input().split())
    graph[from_city].append(to_city)

  #print("n: {}, m: {}, k: {}, x: {}".format(n, m, k, x))  
  #print("graph: ", graph)
  queue = deque()
  queue.append((0, x))

  while queue:
    dist, city = queue.popleft()
    if distance[city] > dist:
      distance[city] = dist
      for to_city in graph[city]:
        queue.append((dist + 1, to_city))

  found = False
  for i in range(1, n + 1):
    if distance[i] == k:
      print(i)
      found = True      
      #print(i, end=' ')
  if not found:
    print(-1)
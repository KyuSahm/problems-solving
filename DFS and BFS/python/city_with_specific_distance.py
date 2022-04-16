'''
특정 거리의 도시 찾기
"이것이 코딩 테스트다"의 page 339
'''
from collections import deque

from collections import deque

def bfs(graph, visited, start, target):
  answer = []
  queue = deque()
  queue.append((start, 0))

  while queue:
    node, distance = queue.popleft()
    if not visited[node]:
      visited[node] = True
      if distance == target:
        answer.append(node)
        continue
      for child_node in graph[node]:
        if not visited[child_node]:
          queue.append((child_node, distance + 1))
  return answer
  
if __name__ == '__main__':
  # n => number of city, m => number of path
  # k => distance between cities
  # x => start city number
  n, m, k, x = map(int, input().split())
  graph = [[] for _ in range(n + 1)]
  visited = [False] * (n + 1)
  
  for _ in range(m):
    f, t = map(int, input().split())
    graph[f].append(t)
  #print (graph)
  answer = bfs(graph, visited, x, k)

  if len(answer) == 0:
    print(-1)
  else:
    print(answer)
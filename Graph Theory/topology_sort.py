'''
위상정렬(topology sort) - 그래프 알고리즘
대학교 수강 신청시의 선수과목과 비슷.

"이것이 코딩테스트다" p 296

입력:
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4

출력:
1 2 5 3 6 4 7
'''
from collections import deque

def topology_sort(graph, indegree, v):
  ans = []
  q = deque()

  # enqueue nodes with no input
  for i in range(1, v + 1):
    if indegree[i] == 0:
      q.append(i)

  while q:
    node = q.popleft()
    ans.append(node)
    for t in graph[node]:
      indegree[t] -= 1
      if indegree[t] == 0:
        q.append(t)

  return ans
  
if __name__ == '__main__':
  v, e = map(int, input().split())

  graph = [ [] for _ in range(v + 1)]
  indegree = [ 0  for _ in range(v + 1)]

  for _ in range(e):
    f, t = map(int, input().split())
    graph[f].append(t)
    indegree[t] += 1

  ans = topology_sort(graph, indegree, v)
  print(ans)
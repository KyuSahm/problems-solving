'''
크루스칼 알고리즘(Kruskal Algorithm)
가장 적은 비용으로 모든 노드를 연결할 수 있는 방법
"이것이 코딩테스트다" page 288

입력:
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25

출력:
159
'''
import heapq

def find_parent(parent, i):
  if parent[i] != i:
    parent[i] = find_parent(parent, parent[i])
  return parent[i]

def union_parent(parent, a, b):
  x = find_parent(parent, a)
  y = find_parent(parent, b)

  if x < y:
    parent[y] = x
  else:
    parent[x] = y

  return  

if __name__ == '__main__':
  v, e = map(int, input().split())

  parent = [i for i in range(v + 1)]
  q = []
  for _ in range(e):
    a, b, c = map(int, input().split())
    heapq.heappush(q, (c, a, b))
  
  total_cost = 0
  while q:
    c, a, b = heapq.heappop(q)  
    if find_parent(parent, a) != find_parent(parent, b):
      union_parent(parent, a, b)
      total_cost += c

  print(total_cost)
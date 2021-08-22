'''
서로 소 집합 알고리즘
"이것이 코딩 테스트다" p273

입력:
6 4
1 4
2 3
2 4
5 6

slow version 출력
부모 테이블: 1 1 2 1 5 5 
각 원소가 속한 집합: 1 1 1 1 5 5

path compression version 출력 
부모 테이블: 1 1 2 1 5 5 
각 원소가 속한 집합: 1 1 1 1 5 5

입력:
6 4
1 4
2 3
3 4
5 6

slow version 출력
부모 테이블: 1 1 2 1 5 5 
각 원소가 속한 집합: 1 1 1 1 5 5

path compression version 출력
부모 테이블: 1 1 2 1 5 5 
각 원소가 속한 집합: 1 1 1 1 5 5

'''

# slow version
def find_parent(parent, x):
  if x != parent[x]:
    return find_parent(parent, parent[x])
  else:
    return x
'''

# path compression version
def find_parent(parent, x):
  if x != parent[x]:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]
'''
def union_parent(parent, i, j):
  a = find_parent(parent, i)
  b = find_parent(parent, j)
  
  # each root information with smaller root 
  if a < b:
    parent[b] = a
  else:
    parent[a] = b    

if __name__ == '__main__':
  # the number of nodes and edges
  v, e = map(int, input().split())
  
  # graph [node number, parent node number]
  graph= [[] for i in range(v + 1)]
  parent = [i for i in range(v + 1)]

  for _ in range(e):
    f, t = map(int, input().split())
    graph[f].append(t)

  #print(graph)  
  #print(parent)

  for i in range(1, v + 1):
    for j in graph[i]:
      union_parent(parent, i, j)

  print("부모 테이블:", end=' ')     
  for i in range(1, v + 1):
    print(parent[i], end=' ')

  print()

  print("각 원소가 속한 집합:", end=' ')     
  for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')  
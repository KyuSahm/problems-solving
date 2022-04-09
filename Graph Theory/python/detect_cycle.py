'''
서로소 집합을 활용한 사이클 판별 소스코드
"이것이 코딩테스트다" page 279

입력:
3 3
1 2
1 3
2 3

출력:
"Cycle is detected"

입력:
6 4
1 2
1 3
3 4
5 6

출력:
"Cycle is not detected"
'''
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

if __name__ == '__main__':
  # number of nodes and edges
  v, e = map(int, input().split())

  # parent init
  parent = [i for i in range(v + 1)]
 
  cycle = False
  for _ in range(e):
    a, b = map(int, input().split())
    
    if find_parent(parent, a) != find_parent(parent, b):
      union_parent(parent, a, b)
    else:
      cycle = True      
      break
  if cycle:
    print("Cycle is detected")
  else:
    print("Cycle is not detected") 
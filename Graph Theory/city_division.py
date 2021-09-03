'''
도시 분할 계획
"이것이 코딩테스트다" p301

입력:
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4

출력:
8
'''
def find_root(root, a):
  if root[a] != a:
    root[a] = find_root(root, root[a])
  return root[a]

def union(root, a, b):
  x = find_root(root, a)
  y = find_root(root, b)

  if x < y:
    root[y] = x
  else:
    root[x] = y  

if __name__ == '__main__':
  # n : number of houses, m: number of edges
  n, m = map(int, input().split())

  root = [i for i in range(n + 1)]
  roads = []
  for _ in range(m):
    a, b, c = map(int, input().split())
    roads.append((a, b, c))

  roads.sort(key=lambda x:x[2])
 
  #print(roads)
  cnt = 0
  ans = 0
  for a, b, c in roads:
    # if cycle not found
    if find_root(root, a) != find_root(root, b):
      union(root, a, b)
      cnt += 1
      ans += c
      # with n - 1 edges, can connect all nodes
      if cnt == n - 2:
        break
  print(ans)
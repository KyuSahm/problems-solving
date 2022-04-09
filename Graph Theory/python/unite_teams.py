'''
팀결성 문제
"이것이 코딩테스트다" p 298

입력:
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1

출력:
NO
NO
YES
'''
def find_root(root, i):
  if root[i] != i:
    root[i] = find_root(root, root[i])
  return root[i]  

def union_root(root, a, b):
  x = find_root(root, a)
  y = find_root(root, b)

  if x < y:
    root[y] = x
  else:
    root[x] = y

if __name__ == '__main__':
  n, m = map(int, input().split())

  root = [i for i in range(n + 1)]

  ans = []
  for _ in range(m):
    a, b, c = map(int, input().split())

    if a == 0:
      union_root(root, b, c)
    elif a == 1:
      if find_root(root, b) == find_root(root, c):
        ans.append('YES')   
      else:
        ans.append('NO')
  
  for a in ans:
    print(a, end='\n')



'''
감시 피하기
"이것이 코딩테스트다" p351

입력1:
5
X S X X T
T X S X X
X X X X X
X T X X X
X X T X X

출력1:
YES

입력2:
4
S S S T
X X X X
X X X X
T T T X

출력2:
NO
'''
# My Implementation
def three_obstacle(graph, n):
  t = []
  for i in range(1, n + 1):
    for j in range(1, n + 1):
      if graph[i][j] != 'S':
        continue
      
      # check right side and add possible obstacle area
      for k in range(j + 1, n + 1):
        if graph[i][k] == 'T':
          if k > j + 1:
            t.append([i, i, j + 1, k - 1, False])
          else:
            return False
      # check left side and add possible obstacle area
      for k in range(j - 1, 0, -1):
        if graph[i][k] == 'T':
          if k < j - 1: 
            t.append([i, i, k + 1, j - 1, False])
          else:
            return False
      # check down side and add possible obstacle area
      for k in range(i + 1, n + 1):
        if graph[k][j] == 'T':
          if k > i + 1: 
            t.append([i + 1, k - 1, j, j, False])
          else:
            return False
      # check upper side and add possible obstacle area      
      for k in range(i - 1, 0, -1):
        if graph[k][j] == 'T':
          if k < i - 1: 
            t.append([k + 1, i - 1, j, j, False])
          else:
            return False

  cnt = 0
  for i in range(len(t)):
    x_s, x_e, y_s, y_e, checked = t[i]
    if not checked:
      cnt += 1
      for j in range(i + 1, len(t)):
         new_x_s, new_x_e, new_y_s, new_y_e, new_checked = t[j]
         # check overapped area
         if not new_checked:
           a = max(x_s, new_x_s)
           b = min(x_e, new_x_e)
           c = max(y_s, new_y_s)
           d = min(y_e, new_y_e)
           
           if a <= b and c <= d:
             t[j][4] = True
             # 3개가 overapped되도록 방해물 설치 못함
             break
  
  if cnt <= 3:
    return True
  else:
    return False
    
if __name__ == '__main__':
  n = int(input())

  graph = [[]]  
  for i in range(1, n + 1):
    row = ['X'] + list(input().split())
    graph.append(row)

  ans = three_obstacle(graph, n)
  if ans:
    print('YES')
  else:
    print('NO')  
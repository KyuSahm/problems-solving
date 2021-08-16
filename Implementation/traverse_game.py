'''
게임 개발
"이것이 코딩 테스트다" p118

Case 1:
입력:
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1

출력:
3

'''
offset = [[(0, -1, 3), (1, 0, 2), (0, 1, 1),  (-1, 0, 0)], # 0: 북쪽
          [(-1, 0, 0), (0, -1, 3), (1, 0, 2), (0, 1, 1)], # 1: 동쪽
          [(0, 1, 1), (-1, 0, 0), (0, -1, 3), (1, 0, 2)], # 2: 남쪽
          [(1, 0, 2), (0, 1, 1), (-1, 0, 0), (0, -1, 3)]] # 3: 서쪽

def traverse(graph, visited, a, b, d):
  visited[a][b] = True  
  for dx, dy, new_d in offset[d]:
      new_x = a + dx
      new_y = b + dy

      if 0 <= new_x < n and 0 <= new_y < m:
        if not visited[new_x][new_y] and graph[new_x][new_y] == 0:
          traverse(graph, visited, new_x, new_y, new_d)


if __name__ == '__main__':
  n, m = map(int, input().split())

  # current position and direction
  a, b, d = map(int, input().split())

  # graph and visited flag
  graph = []
  visited = [[False] * m for _ in range(n)]

  for i in range(n):
    graph.append(list(map(int, input().split())))

  #print(graph)
  #print(visited)
  visited[a][b] = True
  cnt = 1
  
  while True:
    #print(a, b, d)
    found = False    
    for dx, dy, new_d in offset[d]:
        new_x = a + dx
        new_y = b + dy

        if 0 <= new_x < n and 0 <= new_y < m:
          if not visited[new_x][new_y] and graph[new_x][new_y] == 0:
            visited[new_x][new_y] = True            
            cnt += 1
            a, b, d = new_x, new_y, new_d
            found = True
            break

    if not found:
      dx, dy, d = offset[d][3]
      a -= dx
      b -= dy
      #print(a, b, d)
      if graph[a][b] == 1:
        break
  print(cnt)
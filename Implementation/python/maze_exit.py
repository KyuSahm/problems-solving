import time
from collections import deque

def calc_with_dfs(row, col, maze, weight, accum_value, path):
  #print(row, col)
  new_accum_value = accum_value + 1
  
  if new_accum_value >= weight[n - 1][m - 1]:
    return

  if maze[row][col] == 1 and weight[row][col] > new_accum_value:
    weight[row][col] = new_accum_value
    path.append((row, col))
    if row == n - 1 and col == m - 1:
      print("short path: {}".format(path))
  else:
    return  

  if row == n - 1 and col == m - 1:
    return

  if col + 1 < m:
    calc_with_dfs(row, col + 1, maze, weight, weight[row][col], path)
  if row + 1 < n:
    calc_with_dfs(row + 1, col, maze, weight, weight[row][col], path)
  if col - 1 >= 0:
    calc_with_dfs(row, col - 1, maze, weight, weight[row][col], path)
  if row - 1 >= 0:
    calc_with_dfs(row - 1, col, maze, weight, weight[row][col], path)

  return  

def calc_with_bfs(maze, weight, path):
  queue = deque()  
  queue.append((0, 0, 1))
  
  while queue:
    row, col, accum_value = queue.popleft()

    if accum_value < weight[row][col]:
      weight[row][col] = accum_value
      path.append((row, col))
      if row == n - 1 and col == m - 1:
        print("short path: {}".format(path))
    else:
      continue  

    if col + 1 < m and maze[row][col + 1] == 1:
        queue.append((row, col + 1, accum_value + 1))
    if row + 1 < n and maze[row + 1][col] == 1:
        queue.append((row + 1, col, accum_value + 1))
    if col - 1 >= 0 and maze[row][col - 1] == 1:
        queue.append((row, col - 1, accum_value + 1))
    if row - 1 >= 0 and maze[row - 1][col] == 1:
        queue.append((row - 1, col, accum_value + 1))
       
  return 

if __name__ == '__main__':
  INF = int(1e9)
  n, m = map(int, input("N M : ").split())
  
  maze = [[0] * m for i in range(n)]
  weight = [[INF] * m for i in range(n)]
  short_path = []

  #print(maze)
  #print(weight)

  for i in range(n):
    row = input()
    for j in range(m):
      maze[i][j] = int(row[j])
  
  accum_value = 0
  path = []  
  start_time = time.time()
  calc_with_dfs(0, 0, maze, weight, accum_value, path)
  end_time = time.time()

  print("Result: {}".format(weight[n-1][m-1]))
  print("Elapsed time: {}".format(end_time - start_time))

  weight = [[INF] * m for i in range(n)]  
  start_time = time.time()
  path = []
  calc_with_bfs(maze, weight, path)
  end_time = time.time()

  print("Result: {}".format(weight[n-1][m-1]))
  print("Elapsed time: {}".format(end_time - start_time))
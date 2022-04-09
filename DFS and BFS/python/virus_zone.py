'''
바이러스 연구소(삼성전자 SW 역량테스트)
이것이 코딩테스트다 page 341
Test Case 1:
4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2
답: 9

Test Case 2:
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
답: 27

Test Case 3:
8 8
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
답: 3
'''
from itertools import combinations
import copy
import time

def transfer_virus(temp_graph, x, y, n, m):
    offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]    
    
    for dx, dy in offsets:
      new_x = x + dx 
      new_y = y + dy
      
      if new_x >= 0 and new_x < n and new_y >= 0 and new_y < m:
        if temp_graph[new_x][new_y] == 0:
          temp_graph[new_x][new_y] = 2
          transfer_virus(temp_graph, new_x, new_y, n, m)

def count_safe_zone(temp_graph, n, m):
    count = 0
    for i in range(n):
      for j in range(m):
        if temp_graph[i][j] == 0:
          count += 1
          
    return count

def calc_safe_size(graph, sequences, virus_zone, n, m):
  result = 0
  for a, b, c in sequences:
    #print("a: {}, b: {}, c: {}".format(a, b, c))  
    temp_graph = copy.deepcopy(graph)
    temp_graph[a[0]][a[1]] = 1
    temp_graph[b[0]][b[1]] = 1
    temp_graph[c[0]][c[1]] = 1
    
    for virus_x, virus_y in virus_zone:
      #print("virus_x: {}, virus_y: {}".format(virus_x, virus_y))  
      transfer_virus(temp_graph, virus_x, virus_y, n, m)

    result = max(result, count_safe_zone(temp_graph, n, m))

  return result

if __name__ == '__main__':
  # n: number of rows, m: number of columns
  n, m = map(int, input().split())
  
  graph = []    
  for i in range(n):
    graph.append(list(map(int, input().split())))

  print(graph)

  stime = time.time()
  safe_zone = []
  virus_zone = []
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 0:
        safe_zone.append((i, j))
      elif graph[i][j] == 2:  
        virus_zone.append((i, j))

  sequences = list(combinations(safe_zone, 3))
  #print("sequences: {}".format(sequences))
  #print("safe_zone: {}".format(safe_zone))
  #print("virus_zone: {}".format(virus_zone))        
  result = calc_safe_size(graph, sequences, virus_zone, n, m)
  etime = time.time()

  print("result: {}, elapsed time: {}".format(result, etime- stime))
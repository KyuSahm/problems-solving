# BFS(Breadth First Search) Implementation with queue
import time
from collections import deque

def bfs(graph, start_node, sequence):
  queue = deque()
  queue.append(start_node)

  while queue:
    from_node = queue.popleft()

    if not visited[from_node]:
      visited[from_node] = True
      sequence.append(from_node)
      #print("{}".format(from_node), end=' ')
    
      for to_node in graph[from_node]:
        queue.append(to_node)
  return      

if __name__ == '__main__':
  graph = [[],
           [2, 3, 8],
           [1, 7],
           [1, 4, 5],
           [3, 5],
           [3, 4],
           [7],
           [2, 6, 8],
           [1, 7]]
  
  # number of nodes + 1, index 0 is not used.  
  node_len = len(graph)
  for i in range(1, node_len):
    graph[i].sort()

  # visited flag for knowing if the node is visited
  visited = [False] * node_len
  sequence = []

  start_time = time.time()
  bfs(graph, 1, sequence)
  end_time = time.time()
  
  print("sequence: {}".format(sequence))
  print("Elapsed time: {} secs".format(end_time - start_time))
# DFS algorithm implementation
# option 1: recursive call
# option 2: implementation with stack
import time

def dfs_with_recursive_call(graph, visited, from_node, sequence):
  visited[from_node] = True
  #print("{}".format(from_node), end=' ')
  sequence.append(from_node)
  for to_node in graph[from_node]:
    if visited[to_node] == False:
      dfs_with_recursive_call(graph, visited, to_node, sequence)

def dfs_with_stack(graph, visited, start_node, sequence):  
  stack = []
  
  visited[start_node] = True
  stack.append(start_node)
  sequence.append(start_node)

  while stack:
    all_visited = True
    
    for child in graph[stack[-1]]:
      if not visited[child]:
         visited[child] = True
         stack.append(child)
         sequence.append(child)
         all_visited = False
         break
    if all_visited:
      stack.pop()
  return

if __name__ == '__main__':
  graph = [[],
         [8, 3, 2],
         [1,7],
         [5, 4, 1],
         [3, 5],
         [3, 4],
         [7],
         [2, 6, 8], 
         [1, 7] ]

  number_of_node = len(graph)  
  for paths in graph:
    paths.sort()

  visited = [False] * number_of_node

  start_node = 1
  sequence = []
  start_time = time.time()  
  dfs_with_recursive_call(graph, visited, start_node, sequence)
  end_time = time.time()
  print("Sequence = {}".format(sequence))  
  print("Elapsed time with recursive: {}".format(end_time - start_time))

  visited = [False] * number_of_node
  sequence = []
  start_time = time.time()
  dfs_with_stack(graph, visited, start_node, sequence)
  end_time = time.time()
  print("Sequence = {}".format(sequence))    
  print("Elapsed time with stack: {}".format(end_time - start_time))
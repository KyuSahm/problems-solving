import time
import pdb

class MyIceCount:
  def __init__(self, graph, n, m):
    self.n = n
    self.m = m
    self.graph = graph
    self.visited = [[False] * m for _ in range(n)]
    #self.visited = [[False] * m] * n
    self.ice_cnt = 0
    #print("graph: {0}".format(self.graph))
    #print("visited: {0}".format(self.visited))  
    #self.visited = [[False] * len(graph(i))  for i in range(len(graph))] 
  
  def visit(self, i, j):
    if (i >= self.n) or (i < 0) or (j >= self.m) or (j < 0):
      return False

    if graph[i][j] == 1:
      return False

    if not self.visited[i][j]:
      self.visited[i][j] = True
      self.visit(i, j - 1)
      self.visit(i, j + 1)
      self.visit(i - 1, j)
      self.visit(i + 1, j)
      return True

  def counting(self):
    for i in range(n):
        for j in range(m):
          result = self.visit(i, j)
          if result:
            self.ice_cnt += 1
    return self.ice_cnt

if __name__ == '__main__':
  # process user input
  n, m = map(int, input("N M: ").split())
  graph = [[] for _ in range(n)]
  for i in range(n):
    str = input()
    #print("{0}", list(map(int, str)))
    for j in range(len(str)):
      graph[i].append(int(str[j]))
  
  # measure time
  s_time = time.time()
  my_ice_cnt = MyIceCount(graph, n, m)
  #pdb.set_trace()
  count = my_ice_cnt.counting()
  e_time = time.time()
  print("The number of ices: {0}".format(count))
  print("Elapsed time: {0}".format(e_time - s_time))
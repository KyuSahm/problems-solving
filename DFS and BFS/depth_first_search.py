#import pdb
import time
from abc import ABCMeta
from abc import abstractmethod


class AbstractDFS(metaclass=ABCMeta):
  @abstractmethod
  def dfs(self, index):
    pass

class DFS(AbstractDFS):
  def __init__(self, graph):
    self.graph = graph
    self.visited = [False] *len(graph)
    #self.visited = [False for _ in range(len(graph))]

class MyDFS(DFS):
  def __init__(self, graph):
    super().__init__(graph)

  def dfs(self, i):
    print("{0}".format(i), end=' ')
    self.visited[i] = True
    nodes = self.graph[i]
    for j in nodes:
      if self.visited[j] == True:
        continue      
      self.dfs(j)

    return

if __name__ == '__main__':
  graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
  
  #pdb.set_trace()
  s_time = time.time()
  my_dfs = MyDFS(graph)
  my_dfs.dfs(1)
  e_time = time.time()
  print("\nElapsed Time for MyDFS: {0}".format(e_time - s_time))
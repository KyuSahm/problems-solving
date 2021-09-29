import time
from abc import ABCMeta
from abc import abstractmethod
from collections import deque

class AbstractBFS(metaclass=ABCMeta):
  @abstractmethod
  def bfs(self):
    pass

class BFS(AbstractBFS):
  def __init__(self, graph):
    self.graph = graph
    self.visited = [False] * len(graph)
    self.queue = deque()

class MyBFS(BFS):
  def __init__(self, graph):
    super().__init__(graph)

  def bfs(self, i):    
    self.queue.append(i)

    while self.queue:
      j = self.queue.popleft()
      if self.visited[j]:
        continue

      print("{0}".format(j), end = ' ') 
      self.visited[j] = True  
      for k in graph[j]:
        if not self.visited[k]:
          self.queue.append(k)

if __name__ == '__main__':
  graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
  s_time = time.time()
  my_bfs = MyBFS(graph)
  my_bfs.bfs(1)
  e_time = time.time()
  print("\nElapsed time: {0}".format(e_time - s_time))
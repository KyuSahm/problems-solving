#import sys
import time
import heapq

from abc import ABCMeta
from abc import abstractmethod

class AbstractDijkstra(metaclass=ABCMeta):
  @abstractmethod
  def input_path_weight(self):
    pass

  @abstractmethod
  def find_short_path(self):
    pass
  
  @abstractmethod
  def print_short_path(self):
    pass

class Dijkstra(AbstractDijkstra):
  def __init__(self, n, m, start):
    INF = 1e9
    self.n = n
    self.m = m
    self.start = start    
    self.distance = [INF] * (n + 1)
    self.graph = [[] for i in range(n + 1)]
    self.paths = [[] for i in range(n + 1)]    

  def input_path_weight(self):
    for i in range(m):
      start_node, end_node, weight = map(int, input("start_node end_node weight: ").split())
      self.graph[start_node].append((end_node, weight))
    #print ("graph: {0}".format(self.graph))
  
  def find_short_path(self):
    q = []  # heap
    path = [1] 
    heapq.heappush(q, (0, self.start, path))

    while q:
      dist, node, path = heapq.heappop(q)
      #print("popped dist: {} node: {}".format(dist, node))
      if dist < self.distance[node]:
        #visited[node] = True
        self.distance[node] = dist
        self.paths[node].append(path)
        #print("paths[{}]: {}, path: {}".format(node, self.paths[node], path))
              

        for next_node, weight in self.graph[node]:
          next_node_dist = dist + weight
          if next_node_dist < self.distance[next_node]:
            #distance[next_node] = next_node_dist
            next_node_path = path + [next_node]
            #print("next_node_path: {}, [next_node]: {}".format(next_node_path, [next_node]))
            heapq.heappush(q, (next_node_dist, next_node, next_node_path))            
            #print("pushed node dist: {} node: {}".format(next_node_distance, next_node))

  def print_short_path(self):
    print("distance: {}".format(self.distance[1:]))
    print("paths: {}".format(self.paths[1:]))


if __name__ == '__main__':
  n, m = map(int, input("# of nodes and # of paths: ").split())
  start = int(input("start node number: "))
  
  dijkstra = Dijkstra(n, m, start)
  dijkstra.input_path_weight()
  startTime = time.time()
  dijkstra.find_short_path()
  endTime = time.time()
  print("\nElapsed time: {0}".format(endTime-startTime))

  dijkstra.print_short_path()

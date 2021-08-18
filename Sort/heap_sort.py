from abc import ABCMeta
from abc import abstractmethod
from random import randint
import time
import copy
#import pdb

class abstract_sort(metaclass=ABCMeta):
  @abstractmethod
  def sort(self, data):
    pass

class heap_sort(abstract_sort):
  def __init__(self):
    self.heap = [0]
    self.last_leaf_index = 0

  # Sort with insert  
  def sort(self, data):    
    for data_element in data:
      self.insert(data_element)

    sorted_data = []
    while True:
      data_element = self.delete()
      if data_element != None:
        sorted_data.append(data_element)
      else:
        break
    return sorted_data

  # Sort without insert TODO:recursive function
  def sort2(self, data):
    self.heap.extend(data)    
    self.last_leaf_index = len(data)
    
    n = 0
    while True:
      if 2**n > self.last_leaf_index:
        n -= 2
        break
      n += 1

    #print("before sort {0}".format(self.heap))

    while True:
      if n < 0:
        break

      for parent_index in range(2**n, 2**(n + 1)):
        leftchild_index = parent_index * 2
        rightchild_index = parent_index * 2 + 1

        #print("parent_index: {0} leftchild_index: {1} rightchild_index: {2} ".format(parent_index, leftchild_index, rightchild_index))

        if rightchild_index <= self.last_leaf_index:
          if self.heap[rightchild_index] <= self.heap[leftchild_index]:
            if self.heap[rightchild_index] <= self.heap[parent_index]:
              self.heap[rightchild_index], self.heap[parent_index] = self.heap[parent_index], self.heap[rightchild_index]
          else:
            if self.heap[leftchild_index] <= self.heap[parent_index]:
              self.heap[leftchild_index], self.heap[parent_index] = self.heap[parent_index], self.heap[leftchild_index]
        elif leftchild_index <= self.last_leaf_index:
          if self.heap[leftchild_index] <= self.heap[parent_index]:
            self.heap[leftchild_index], self.heap[parent_index] = self.heap[parent_index], self.heap[leftchild_index]
        #print("sort {0}".format(self.heap))
      n -= 1
    #print("after sort {0}".format(self.heap))
    sorted_data = []
    while True:
      data_element = self.delete()
      if data_element != None:
        sorted_data.append(data_element)
      else:
        break
    return sorted_data

  def insert(self, data_element):
    self.heap.append(data_element)
    self.last_leaf_index += 1
    parent_index = int(self.last_leaf_index / 2)
    child_index = self.last_leaf_index

    while parent_index >= 1:
      if self.heap[child_index] < self.heap[parent_index]:
        self.heap[child_index], self.heap[parent_index] = self.heap[parent_index], self.heap[child_index]
        child_index = parent_index
        parent_index = int(child_index / 2)
      else:
        break

  def delete(self):
    if self.last_leaf_index <= 0:
      return None
      
    data_element = self.heap[1]
    self.heap[1] = self.heap[self.last_leaf_index]
    self.last_leaf_index -= 1

    parent_index = 1
    
    while True:
      leftchild_index = parent_index * 2
      rightchild_index = parent_index * 2 + 1

      if rightchild_index <= self.last_leaf_index:
        if self.heap[rightchild_index] >= self.heap[leftchild_index]:
          if self.heap[leftchild_index] < self.heap[parent_index]:
            self.heap[leftchild_index], self.heap[parent_index] = self.heap[parent_index], self.heap[leftchild_index]
            parent_index = leftchild_index
          else:
            break
        else:
          if self.heap[rightchild_index] < self.heap[parent_index]:
            self.heap[rightchild_index], self.heap[parent_index] = self.heap[parent_index], self.heap[rightchild_index]
            parent_index = rightchild_index
          else:
            break
      elif leftchild_index <= self.last_leaf_index:
        if self.heap[leftchild_index] < self.heap[parent_index]:
            self.heap[leftchild_index], self.heap[parent_index] = self.heap[parent_index], self.heap[leftchild_index]
            parent_index = leftchild_index
        else:
            break
      else:
        break
    return data_element  


if __name__ == '__main__':
  #pdb.set_trace()
  data = []

  # insert 10,000 integers into array
  for _ in range(10):
    data.append(randint(1, 100))

  data3 = copy.deepcopy(data)
  data4 = copy.deepcopy(data)

  start_time = time.time()
  heap_sort_instance = heap_sort()
  data3 = heap_sort_instance.sort(data3)
  end_time = time.time()
  print("{0}".format(data3))
  print("heap sort with insert - Elapsed time: {0}".format(end_time - start_time))

  start_time = time.time()
  heap_sort_instance2 = heap_sort()
  data4 = heap_sort_instance2.sort2(data4)
  end_time = time.time()
  print("{0}".format(data4))
  print("heap sort without insert - Elapsed time: {0}".format(end_time - start_time))
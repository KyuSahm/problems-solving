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

class selection_sort(abstract_sort):
  def sort(self, data):
    data_len = len(data)
    for i in range(data_len):
      min_index = i
      for j in range(i + 1, data_len):
        if (data[min_index] > data[j]):
            min_index = j
      if (min_index != i):
        data[i], data[min_index] = data[min_index], data[i]

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

  # Sort without insert TODO: error
  def sort2(self, data):
    self.heap.extend(data)    
    self.last_leaf_index = len(data)
    
    n = 0
    while True:
      if 2**n > self.last_leaf_index:
        n -= 1
        break
      n += 1

    while True:
      if n < 0:
        break

      for parent_index in range(2**n, 2**(n + 1)):
        leftchild_index = parent_index * 2
        rightchild_index = parent_index * 2 + 1

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
      n -= 1

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
  for _ in range(500):
    data.append(randint(1, 100))

  data2 = copy.deepcopy(data)
  data3 = copy.deepcopy(data)
  data4 = copy.deepcopy(data)

  # Sort with selection sort O(N^2)
  startTime = time.time()
  data.sort()
  endTime = time.time()
  #print("sorted data array:", data)
  print("python internal sort lib - Elapsed Time:", endTime - startTime)

  # Sort with selection sort O(N^2)
  startTime = time.time()
  s_sort = selection_sort()
  s_sort.sort(data2)
  endTime = time.time()
  #print("sorted data array:", data)
  print("selection_sort - Elapsed Time:", endTime - startTime)  

  start_time = time.time()
  heap_sort_instance = heap_sort()
  data3 = heap_sort_instance.sort(data3)
  end_time = time.time()
  #print("{0}".format(data3))
  print("heap sort with insert - Elapsed time: {0}".format(end_time - start_time))

  start_time = time.time()
  heap_sort_instance2 = heap_sort()
  data4 = heap_sort_instance2.sort2(data4)
  end_time = time.time()
  #print("{0}".format(data4))
  print("heap sort without insert - Elapsed time: {0}".format(end_time - start_time))
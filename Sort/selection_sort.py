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

if __name__ == '__main__':
  #pdb.set_trace()
  data = []

  # insert 10,000 integers into array
  for _ in range(500):
      data.append(randint(1, 100))

  data2 = copy.deepcopy(data)

  #print("data array:", data)

  # Sort with selection sort O(N^2)
  startTime = time.time()
  s_sort = selection_sort()
  s_sort.sort(data)
  endTime = time.time()
  #print("sorted data array:", data)
  print("Selection Sort - Elapsed Time:", endTime - startTime)

  # Sort with selection sort O(N^2)
  #print("data2 array:", data2)
  startTime = time.time()
  data2.sort()
  endTime = time.time()
  #print("sorted data array:", data2)
  print("Internal Sort Lib - Elapsed Time:", endTime - startTime)
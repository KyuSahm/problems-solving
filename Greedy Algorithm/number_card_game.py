#import pdb
import time
from abc import ABCMeta
from abc import abstractmethod

class AbstractCardGame(metaclass=ABCMeta):
  @abstractmethod
  def find_max_val(self, n, m, data):
    pass

class CardGameWithAPI(AbstractCardGame):
  def find_max_val(self, n, m, data):
    #pdb.set_trace()  
    result = []  
    for i in range(n):
      result.append(min(data[i])) 
    max_val = max(result)

    return max_val

class CardGameWithCalc(AbstractCardGame):
  def find_max_val(self, n, m, data):
    #pdb.set_trace()  
    max_val = 0  
    for i in range(n):
      min_val = 10001
      for j in range(m):
        if (min_val > data[i][j]):
          min_val = data[i][j]
      if (max_val < min_val):
        max_val = min_val
    return max_val  

if __name__ == '__main__':
  print("Input number of Rows(1<=N) and Columns(M <= 100)")
  n, m = map(int, input().split())

  data = []

  print("Input data")
  for i in range(n):
    data.append(list(map(int, input().split())))
  
  s_time = time.time()
  card_game = CardGameWithAPI()
  max_val = card_game.findMaxValue(n, m, data)
  e_time = time.time()

  print("Maximum value: {0}".format(max_val))
  print("Elapsed Time: {0}".format(e_time - s_time))

  s_time = time.time()
  card_game = CardGameWithCalc()
  max_val = card_game.findMaxValue(n, m, data)
  e_time = time.time()

  print("Maximum value: {0}".format(max_val))
  print("Elapsed Time: {0}".format(e_time - s_time))
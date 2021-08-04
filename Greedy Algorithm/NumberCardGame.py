#import pdb
import time
from abc import ABCMeta
from abc import abstractmethod

class AbstractCardGame(metaclass=ABCMeta):
  @abstractmethod
  def findMaxValue(self, n, m, data):
    pass

class CardGameWithAPI(AbstractCardGame):
  def findMaxValue(self, n, m, data):
    #pdb.set_trace()  
    result = []  
    for i in range(n):
      result.append(min(data[i])) 
    maxValue = max(result)

    return maxValue  

class CardGameWithCalc(AbstractCardGame):
  def findMaxValue(self, n, m, data):
    #pdb.set_trace()  
    maxValue = 0  
    for i in range(n):
      minValue = 10001
      for j in range(m):
        if (minValue > data[i][j]):
          minValue = data[i][j]
      if (maxValue < minValue):
        maxValue = minValue
    return maxValue  

if __name__ == '__main__':
  print("Input number of Rows(1<=N) and Columns(M <= 100)")
  n, m = map(int, input().split())

  data = []

  print("Input data")
  for i in range(n):
    data.append(list(map(int, input().split())))
  
  startTime = time.time()
  cardGame = CardGameWithAPI()
  maxValue = cardGame.findMaxValue(n, m, data)
  endTime = time.time()

  print("Maximum value: {0}".format(maxValue))
  print("Elapsed Time: {0}".format(endTime - startTime))

  startTime = time.time()
  cardGame = CardGameWithCalc()
  maxValue = cardGame.findMaxValue(n, m, data)
  endTime = time.time()

  print("Maximum value: {0}".format(maxValue))
  print("Elapsed Time: {0}".format(endTime - startTime))

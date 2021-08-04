from abc import ABCMeta
from abc import abstractmethod
import time

class AbstractBigNumber(metaclass=ABCMeta):
  @abstractmethod
  def calc(self, m, k, numbers):
    pass

class BigNumber(AbstractBigNumber):
  def calc(self, m, k, numbers):
    numbers.sort()
    #print("numbers: {0}".format(numbers))
    maxValue = numbers[-1]
    secondValue = numbers[-2]

    valueArray = []
    sumValue = 0
    for i in range(1, m + 1):
      if i % (k + 1) == 0:
        sumValue += secondValue
        valueArray.append(secondValue)
      else:
        sumValue += maxValue
        valueArray.append(maxValue)
    result = {}
    result['value'] = valueArray
    result['sum'] = sumValue
    return result

class FastBigNumber(AbstractBigNumber):
  def calc(self, m, k, numbers):
    numbers.sort()
    #print("numbers: {0}".format(numbers))
    maxValue = numbers[-1]
    secondValue = numbers[-2]
    circleValue = m // (k +1)

    sumValue = circleValue * secondValue + (m - circleValue) *maxValue
    result = {}
    result['sum'] = sumValue
    return result


if __name__ == "__main__":
  # N: Number of Natural Number, M: Number of adding, K: Maximum number of adding number with same index
  print("Input N(2<=N<=1,000, M(1<=M<=10,000), K(1<=K<=10,000):")
  n, m, k = map(int, input().split())

  #print("N: {0}, M: {1}, K: {2}, ".format(n, m, k))
  numbers = list(map(int, input("Number:").split()))
  
  startTime = time.time()
  bigNumber = BigNumber()
  result = bigNumber.calc(m, k, numbers)
  endTime = time.time()
  print("BigNumber result: {0}".format(result))
  print("Elapsed Time: {0}".format(endTime-startTime))

  startTime = time.time()
  fastBigNumber = FastBigNumber()
  result = fastBigNumber.calc(m, k, numbers)
  endTime = time.time()
  print("FastBigNumber result: {0}".format(result))
  
  #  print("module name: {0}".format(__name__))
  print("Elapsed Time: {0}".format(endTime-startTime))

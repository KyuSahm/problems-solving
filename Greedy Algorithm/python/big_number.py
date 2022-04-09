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
    max_val = numbers[-1]
    second_val = numbers[-2]

    va = []
    sum_val = 0
    for i in range(1, m + 1):
      if i % (k + 1) == 0:
        sum_val += second_val
        va.append(second_val)
      else:
        sum_val += max_val
        va.append(max_val)
    result = {}
    result['value'] = va
    result['sum'] = sum_val
    return result

class FastBigNumber(AbstractBigNumber):
  def calc(self, m, k, numbers):
    numbers.sort()
    #print("numbers: {0}".format(numbers))
    max_val = numbers[-1]
    second_val = numbers[-2]
    circle_val = m // (k +1)

    sum_val = circle_val * second_val + (m - circle_val) * max_val
    result = {}
    result['sum'] = sum_val
    return result

if __name__ == "__main__":
  # N: Number of Natural Number, M: Number of adding, K: Maximum number of adding number with same index
  print("Input N(2<=N<=1,000, M(1<=M<=10,000), K(1<=K<=10,000):")
  n, m, k = map(int, input().split())

  #print("N: {0}, M: {1}, K: {2}, ".format(n, m, k))
  numbers = list(map(int, input("Number:").split()))
  
  s_time = time.time()
  big_number = BigNumber()
  result = big_number.calc(m, k, numbers)
  e_time = time.time()
  print("BigNumber result: {0}".format(result))
  print("Elapsed Time: {0}".format(e_time - s_time))

  s_time = time.time()
  fast_big_number = FastBigNumber()
  result = fast_big_number.calc(m, k, numbers)
  e_time = time.time()
  print("FastBigNumber result: {0}".format(result))
  
  #  print("module name: {0}".format(__name__))
  print("Elapsed Time: {0}".format(e_time-s_time))
'''
시각
"이것이 코딩테스트다" page 113

입력:
5
출력:
11475
'''
import time
from abc import ABCMeta
from abc import abstractmethod

class AbstractClockChecker(metaclass=ABCMeta):
  @abstractmethod
  def count_number_three(self):
    pass

class MyClockChecker(AbstractClockChecker):
  def count_number_three(self, n):
    count = 0
    for h in range(n + 1):
      hour = str(h)
      if (hour.find('3') != -1):
        count += 3600
        continue
      
      for m in range(60):
        minute = str(m)
        if (minute.find('3') != -1):
          count += 60
          continue
        
        for s in range(60):
          second = str(s)
          if (second.find('3') != -1):
            count += 1
    return count        

class BookClockChecker(AbstractClockChecker):
  def count_number_three(self, n):
    count = 0
    for h in range(n+1):
      for m in range(60):
        for s in range(60):
          if ('3' in str(h) + str(m) + str(s)):
            count += 1
    return count

if __name__ == '__main__':
  n = int(input("N: "))

  s_time = time.time()
  my_clock_checker = MyClockChecker()
  count = my_clock_checker.count_number_three(n)  
  e_time = time.time()
  print("Count: {0}, elapsed Time: {1}".format(count, e_time - s_time))

  s_time = time.time()
  book_clock_checker = BookClockChecker()
  count = book_clock_checker.count_number_three(n)  
  e_time = time.time()
  print("Count: {0}, elapsed Time: {1}".format(count, e_time - s_time))
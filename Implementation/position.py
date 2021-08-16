'''
상하좌우
"이것이 코딩테스트다" page 110

입력:
5
R R R U D D
'''
import time
from abc import ABCMeta
from abc import abstractmethod

class AbstractPath(metaclass=ABCMeta):
  @abstractmethod
  def move(self, path):
    pass

class MyPath(AbstractPath):
  def move(self, n, path):
    position = [1, 1]

    for command in path:
      if (command == 'L' and position[1] > 1):
        position[1] -= 1
      elif (command == 'R' and position[1] < n):
        position[1] += 1
      elif (command == 'U' and position[0] > 1):
        position[0] -= 1
      elif (command == 'D' and position[0] < n):
        position[0] += 1
    return position

class BookPath(AbstractPath):
  def move(self, n, path):
    commands = ['L', 'R', 'U', 'D']
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    x, y = 1, 1
    nextX, nextY = 0, 0
    for command in path:
      for i in range(len(commands)):
        if (command == commands[i]):
          nextX = x + dx[i]
          nextY = y + dy[i]
          break
      if (not (nextX < 1 or nextX > n or nextY < 1 or nextY > n)):
        x, y = nextX, nextY

    position = [y, x]
    return position


if __name__ == '__main__':
  n = int(input())
  path = input().split()

  s_time = time.time()
  my_path = MyPath()
  position = my_path.move(n, path);
  e_time = time.time()

  print("last Position: (row, col) = ({0}, {1})".format(position[0], position[1]))
  print("elapsed Time: {0}".format(e_time - s_time))

  s_time = time.time()
  book_path = BookPath()
  position = book_path.move(n, path);
  e_time = time.time()

  print("last Position: (row, col) = ({0}, {1})".format(position[0], position[1]))
  print("elapsed Time: {0}".format(e_time - s_time))
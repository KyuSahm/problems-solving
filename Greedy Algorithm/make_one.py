
import time

def check_count(n, m):
  count = 0
  while True:
    if n % m == 0:
      n = n / m
    else:
      n -= 1

    count += 1

    if n == 1:
      break
  return count

def check_count_fast(n, m):
  count = 0
  while True:
    r = int(n % m)
    if r == 0:
      n = n / m
      count += 1
    elif n < m:
      count += r - 1
      break  
    else:
      n -= r
      count += r  
  return count

if __name__ == '__main__':
  n, m = map(int, input().split())

  print(n, m)

  stime = time.time()
  count = check_count(n, m)
  etime = time.time()
  print("answer: {}, elapsed time: {}".format(count, etime - stime))

  stime = time.time()
  count = check_count_fast(n, m)
  etime = time.time()
  print("answer: {}, elapsed time: {}".format(count, etime - stime))
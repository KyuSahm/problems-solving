import time

if __name__ == '__main__':
  c = list(map(int, input("The types of coins: ").split()))
  p = int(input("Price: "))

  s_time = time.time()
  c.sort(reverse=1)
  t = [0 for _ in range(len(c))]

  for i in range(len(c)):
    n = p // c[i]
    t[i] = n
    p -= n * c[i]
    '''
    if (n != 0):
      print("{0} won : {1}".format(coin_types[i], n))
    '''
    if p <= 0:
      break;

  print("{0} : {1}".format(c, t))
  e_time = time.time()
  print("Elapsed Time: {0}".format(e_time - s_time))
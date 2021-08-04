import time

if __name__ == '__main__':
  coinTypes = list(map(int, input("The types of coins: ").split()))
  price = int(input("Price: "))

  startTime = time.time()
  coinTypes.sort(reverse=1)
  coinTypeLen = len(coinTypes)
  numberOfCoinTypes = [0 for _ in range(coinTypeLen)]

  for i in range(coinTypeLen):
    numberOfCoin = price // coinTypes[i]
    numberOfCoinTypes[i] = numberOfCoin
    price -= numberOfCoin * coinTypes[i]
    '''
    if (numberOfCoin != 0):
      print("{0} won : {1}".format(coinTypes[i], numberOfCoin))
    '''
    if (price <= 0):
      break;

  print("{0} : {1}".format(coinTypes, numberOfCoinTypes))
  endTime = time.time()
  print("Elapsed Time: {0}".format(endTime - startTime))

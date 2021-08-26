if __name__ == '__main__':
  # input number of array
  n = int(input())
  food_storage = list(map(int, input().split()))

  a = [ 0 for _ in food_storage]
  #print(n, food_storage[1], a)

  a[0] = food_storage[0]
  a[1] = max(a[0], food_storage[1])

  for i in range(2, n):
    a[i] = max(a[i - 2] + food_storage[i], a[i - 1])

  print(a[n - 1])

  dic = {}
  dic['파이썬'] = 'www.python.org'
  dic['마이크로소프트'] = 'www.microsoft.com'

  print(dic)  
  print(list(dic.keys()))
  print(list(dic.values()))

  print('파이썬' in dic.keys())
  print('www.python.org' in dic.values())
  dic.clear()
  print(dic) 
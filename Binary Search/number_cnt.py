if __name__ == '__main__':
  n, m = map(int, input().split())
  values = list(map(int, input().split()))

  print(n, m, values)

  index = -1
  start = 0
  end = len(values) - 1
  
  while start <= end:
    mid = (start + end) // 2
    
    if values[mid] > m:
      end = mid - 1
    elif values[mid] < m:
      start = mid + 1
    else:    
       index = mid
       break
  
  print("index: {}".format(index))
  
  if index != -1:
    count = 1
    # 왼쪽에 존재하는 수를 셈
    for i in range(index - 1, -1, -1):
      if values[i] == m:
        count += 1
      else:
        break
    
    # 오른쪽에 존재하는 수를 셈
    for i in range(index + 1, len(values)):
      if values[i] == m:
        count += 1
      else:
        break
  else:
    count = -1
  print("answer is {}".format(count))
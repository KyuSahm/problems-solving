def from_big_to_low(dduck, n, m):
  answer = 0
  prev_sum = 0
  for i in range(1, len(dduck)):
    pivot = dduck[i]

    print("pivot: {}".format(pivot))
    sum = 0  
    j = 0
    while j < len(dduck):
      remainder = dduck[j] - pivot
      if remainder >= 0:
        sum += remainder
      else:
        break
      j += 1
    
    print(i, j, sum, prev_sum)
    if m == sum:
      answer = pivot
      break
    elif m > prev_sum and m < sum:
      if (m - prev_sum) % i == 0:
        answer = dduck[i - 1] - int((m - prev_sum) / i)
      else:
        answer = dduck[i - 1] - int((m - prev_sum) / i) - 1  
      break
    elif i == len(dduck) - 1:
      if (m - sum) % i == 0:
        answer = dduck[i] - int((m - sum) / i)
      else:
        answer = dduck[i] - int((m - sum) / i) - 1  
      break

    prev_sum = sum
  return answer    

def binary_search(dduck, n, m):
  left = dduck[0]
  right = 0  
  
  # binary search
  while left >= right:
    sum = 0
    pivot = (left + right) // 2
    
    for i in range(n):
      if dduck[i] > pivot:
        sum += dduck[i] - pivot
      else:
        break
    
    print(pivot, left, right, sum)

    if sum > m:
      result = pivot
      right = pivot + 1      
    elif sum < m:
      left = pivot - 1
    else:
      result = pivot
      break
    
  return result

# 떡볶기 떡 만들기
if __name__ == '__main__':
  n, m = map(int, input().split())

  dduck = list(map(int, input().split()))
  dduck.sort(reverse=True)
  print("dduck: {}".format(dduck))

  #answer = from_big_to_low(dduck, n, m)
  #print(answer)

  answer = binary_search(dduck, n, m)
  print(answer)  
'''
"바닥공사"
이것이 코딩테스트다 page 223
'''
if __name__ == '__main__':
  n = int(input())
  a = [0, 1, 3]

  for i in range(3, n + 1):
    b = (a[i - 1] + 2 * a[i - 2]) % 796796
    a.append(b)
  
  answer = a[n]
  print(answer)     
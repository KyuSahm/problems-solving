
'''
연산자 끼워 넣기
"이것이 코딩테스트다" page 349

예1)
입력:
2
5 6
0 0 1 0

출력:
30
30

예2)
입력:
3
3 4 5
1 0 1 0

출력:
35
17

예3)
입력:
6
1 2 3 4 5 6
2 1 1 1

출력:
54
-24

'''
import time

# Set for product(permutation with duplicate values)
op_sequence = set()

# calc operator sequences using permutation
def permute(head, tail):
  tail_len = len(tail)
  if tail_len == 1:
    #print(head, tail)
    op_sequence.add(head + tail)
    return

  for i in range(tail_len):
    new_head = head + tail[i]
    new_tail = tail[0:i] + tail[i + 1:tail_len]
    permute(new_head, new_tail)

def calc_with_permute(a, n_add, n_minus, n_mul, n_div):
  op_array = ''  
  for _ in range(n_add):
    op_array += '+'
  for _ in range(n_minus):
    op_array += '-'
  for _ in range(n_mul):
    op_array += '*'
  for _ in range(n_div):
    op_array += '/'

  permute('', op_array)

  op_seq_list = list(op_sequence)
  #print(op_seq_list, len(op_seq_list))

  max_val = -int(1e9)
  min_val = int(1e9)
  for i in range(len(op_seq_list)):
    op_result = a[0]
    #print(a[0], end=' ')
    for j in range(0, len(op_seq_list[i])):
      if op_seq_list[i][j] == '+':
        op_result += a[j + 1]
      elif op_seq_list[i][j] == '-':
        op_result -= a[j + 1]
      elif op_seq_list[i][j] == '*':
        op_result *= a[j + 1]
      elif op_seq_list[i][j] == '/':
        op_result = int(op_result / a[j + 1])
      #print(op_seq_list[i][j], a[j + 1], end=' ')
    #print('=', op_result)
    max_val = max(max_val, op_result)
    min_val = min(min_val, op_result)

  return max_val, min_val

max_op_result = int(-1e9)
min_op_result = int(1e9)

def dfs(operators, a, index, op_result):
  found = False
  for i in range(len(operators)):
    if operators[i][1] > 0:
      found = True
      operators[i][1] -= 1
      if operators[i][0] == '+':
        next_op_result = op_result + a[index]
      elif operators[i][0] == '-':
        next_op_result = op_result - a[index]
      elif operators[i][0] == '*':
        next_op_result = op_result * a[index]
      elif operators[i][0] == '/':  
        next_op_result = int(op_result / a[index])
      
      #print(operators[i][0], ' ',  a[index], end=' ')
      dfs(operators, a, index + 1, next_op_result)
      operators[i][1] += 1
  if not found:
    #print('= ', op_result)
    global max_op_result, min_op_result
    max_op_result = max(op_result, max_op_result)
    min_op_result = min(op_result, min_op_result)

  return  

if __name__ == '__main__':
  # print(int(-1/3)) 0 printed
  # print(-1//3) -1 printed  
  n = int(input())
  a = list(map(int, input().split()))

  n_add, n_minus, n_mul, n_div = map(int, input().split())

  s_time = time.time()
  max_val, min_val = calc_with_permute(a, n_add, n_minus, n_mul, n_div)
  e_time = time.time()
  print("max_val = {}, min_val = {}, elapsed time = {} sec".format(max_val, min_val, e_time - s_time))
  
  operators = [['+', n_add], ['-', n_minus], ['*', n_mul], ['/', n_div]]
  op_result = a[0]

  s_time = time.time() 
  if len(a) > 1:
    dfs(operators, a, 1, op_result)
    max_val, min_val = max_op_result, min_op_result
  else:
    max_val, min_val = op_result, op_result
  e_time = time.time()  
  print("max_val = {}, min_val = {}, elapsed time = {} sec".format(max_val, min_val, e_time - s_time))
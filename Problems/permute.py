import copy
import time

#permute_set = set()
permute_list = []

def permute1(head, tail, start, end):
  if start == end:
    #print(tuple(head + tail))
    permute_list.append(head + tail)
    #permute_set.add(tuple(head + tail))
    return

  for i in range(start, end + 1):
    new_head = head + [tail[i]]
    new_tail = tail[:i] + tail[i + 1:]        
    permute1(new_head, new_tail, 0, len(new_tail) - 1)

  return

def permute2(data, start, end):
  if start == end:
    permute_list.append(copy.deepcopy(data))
    return

  for i in range(start, end + 1):
    data[start], data[i] = data[i], data[start]
    permute2(data, start + 1, end)
    data[start], data[i] = data[i], data[start]


if __name__ == '__main__':
  sequence = 0
  data = [1, 2, 3, 4, 5]
  data_copy = copy.deepcopy(data)

  start_time = time.time()
  permute1([], data, 0, len(data) - 1)
  end_time = time.time()
  for element in permute_list:
    print(element)

  print("total number of permutation: {}".format(len(permute_list)))
  print("permute1 algorithms elapsed: {}".format(end_time - start_time)) 

  permute_list = []
  start_time = time.time()
  permute2(data_copy, 0, len(data_copy) - 1)
  end_time = time.time()

  #for element in permute_set:
  for element in permute_list:
    print(element)

  print("total number of permutation: {}".format(len(permute_list)))
  print("permute2 algorithms elapsed: {}".format(end_time - start_time))

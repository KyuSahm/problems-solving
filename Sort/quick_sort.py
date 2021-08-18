import copy

def quick_sort1(array_data, start, end):
  if start >= end:
      return

  pivot = array_data[start]
  left = start + 1
  right = end

  while left <= right:
    while left <= end and array_data[left] <= pivot:
      left += 1

    while right > start and array_data[right] >= pivot:
      right -= 1

    if left < right:
      array_data[left], array_data[right] = array_data[right], array_data[left]
    else:
      array_data[start], array_data[right] = array_data[right], array_data[start]
      quick_sort1(array_data, start, right - 1)
      quick_sort1(array_data, right + 1, end)

  return

def quick_sort2(array_data):
  if len(array_data) <= 1:
    return array_data

  pivot = array_data[0]
  target_array = array_data[1:]

  head = [i for i in target_array if i <= pivot]
  tail = [i for i in target_array if i > pivot]

  return quick_sort2(head) + [pivot] + quick_sort2(tail)

if __name__ == '__main__':
  array_data = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
  array_data_copy = copy.deepcopy(array_data)
  print(array_data)

  quick_sort1(array_data, 0, len(array_data) - 1)  
  print(array_data)

  sorted_data = quick_sort2(array_data_copy)
  print(sorted_data)
'''
공유기 설치 문제
이것이 코딩테스트다. page 369
'''
if __name__ == '__main__':
  n, c = map(int, input().split())
  pos = [] 

  #print(n, c)

  for i in range(n):
    pos.append(int(input()))
  
  pos.sort()
  min_val = min(pos)
  max_val = max(pos)

  answer = 0
  dist_min = 1
  dist_max = max_val - min_val
  
  while dist_min <= dist_max:
    wifi_cnt = 1
    cur_pos = min_val
    mid = (dist_min + dist_max) // 2
    
    #print("mid: {}".format(mid))
    cur_pos += mid    
    for i in range(1, len(pos)):
      if pos[i] >= cur_pos:
        #print("cur_pos: {} pos:{}".format(cur_pos, pos[i]))
        wifi_cnt += 1
        cur_pos += pos[i]

    #print("wifi: {} c:{}".format(wifi_cnt, c))
    if wifi_cnt >= c:      
      answer = max(mid, answer)
      dist_min = mid + 1
    else:
      dist_max = mid - 1

  print("answer: {}".format(answer))

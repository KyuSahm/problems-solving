'''
문자열 압축
2020 카카오 신입 공채
"이것이 코딩테스트다" p323

입력1:
aabbaccc

출력1:
7

입력2:
ababcdcdababcdcd

출력2:
9

입력3:
abcabcdede

출력3:
8

입력4:
abcabcabcabcdededededede

출력4:
14

입력5:
xababcdcdababcdcd

출력5:
17
'''

if __name__ == '__main__':
  s = input()
  h = len(s) // 2
  ans = len(s)
  # step means the length of compression
  for step in range(1, h + 1):
    cnt = 1
    k = 0
    l = k + step
    result = ''
    while l < len(s):
      matched = True
      if l + step - 1 < len(s):
        for j in range(step): 
          if s[k + j] != s[l + j]:
            matched = False
            break
      else:
        matched = False

      if matched:
        cnt += 1        
      else:
        if cnt > 1:
          result += str(cnt) + s[k:l]
        else:
          result += s[k:l]
        cnt = 1
      k = l
      l = k + step

    if cnt > 1:
      result += str(cnt) + s[k:len(s)]
    else:  
      result += s[k:len(s)]    
    ans = min(ans, len(result))

  print("ans: ", ans)
'''
괄호 변환
"이것이 코딩 테스트다"의 page 346
카카오 코딩 테스트 문제
'''
result = []

def is_right_paren(w):
  left_paren = 0
  right_paren = 0

  for i in range(len(w)):
    if w[i] == '(':
      left_paren += 1
    elif w[i] == ')':
      right_paren += 1

    if right_paren > left_paren:
      return False
  return True

def parenthesis(w):
  left_paren = 0
  right_paren = 0

  u = ''
  v = ''

  for i in range(len(w)):
    if w[i] == '(':
      left_paren += 1
    elif w[i] == ')':
      right_paren += 1
    
    u += w[i]
    if left_paren == right_paren:
      v = w[i+1:len(w)]

      if is_right_paren(u):
        u += parenthesis(v)
        return u
      else:
        a = '('
        a += parenthesis(v)
        a += ')'
        
        for k in u[1:len(u)-1]:
          if k == '(':
            a += ')'
          else:
            a += '('
        return a
  return ''    

if __name__ == '__main__':
  w = input()
  
  if is_right_paren(w):
    print(w)
  else:
    print(parenthesis(w))

'''
성적이 낮은 순서로 학생 출력하기
"이것이 코딩테스트다" page 180

예1)
입력:
11
홍길동 95
이순신 77
김규삼 100
최문순 50
김갑수 80
박대수 10
정몽주 20
성삼문 99
정도전 70
김혜수 85
류중일 98


출력:
박대수 정몽주 최문순 정도전 이순신 김갑수 김혜수 홍길동 류중일 성삼문 김규삼
'''
import time

def count_sort(name_score):
  scores = [[] for _ in range(101)]
  for name, s in name_score:
    scores[s].append(name)

  sorted_names = []  
  for i in range(1, 101):
    for name in scores[i]:
      sorted_names.append(name)
  return sorted_names    
  
if __name__ == '__main__':
  n = int(input())

  name_score = []
  for i in range(n):
    nm, s = input().split()
    s = int(s)
    name_score.append((nm, s))
  
  # use python sort function
  s_time = time.time()  
  name_score_sorted = sorted(name_score, key=lambda x:(x[1]))
  e_time = time.time()
  
  for name, score in name_score_sorted:
    print(name, end=' ')
  print("elapsed time: {}".format(e_time - s_time))

  # use counting sort
  s_time = time.time()
  name_sorted = count_sort(name_score)
  e_time = time.time()

  for name in name_sorted:
    print(name, end=' ')
  print("elapsed time: {}".format(e_time - s_time))
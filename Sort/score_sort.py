'''
"국영수 성적 정렬 문제"
이것이 코딩 테스트다 p359
조건:
 국어 점수는 감소 순서로,
 영어 점수는 증가 순서로,
 수학 점수는 감소 순서로

입력:
12
Junkyu 50 60 100
Sangkeun 80 60 50
Sunyoung 80 70 100
Soong 50 60 90
Haebin 50 60 100
Kangsoo 60 80 90
Donghyuk 80 60 100
Sei 70 70 70
Wonseob 70 70 90
Sanghyun 70 70 80
nsj 80 80 80
Taewhan 50 60 90
'''
if __name__ == '__main__':
  n = int(input())

  scores = []
  for _ in range(n):
    name, k, e, m = input().split()
    scores.append((name, int(k), int(e), int(m)))

  scores.sort(key = lambda x:(-x[1], x[2], -x[3]), reverse=True)

  for score in scores:
    print(score)
'''
구슬 주머니
구슬 주머니에 번호가 써진 구슬이 N개 있을 때, 어느 한 구슬에 쓰여진 번호가 다른 나머지 구슬에 쓰여진 번호의 합과 같다면 그 구슬 주머니는 '좋은 주머니'이다. 예를 들어, 구슬 주머니 안에 [3, 1, 7, 3]라는 번호가 쓰여진 구슬이 들어있다면, 7을 제외한 나머지 번호의 합이 7(1+3+3)이므로 이 구슬 주머니는 좋은 구슬 주머니이다.
당신은 현재 N개의 구슬이 담긴 구슬 주머니를 가지고 있는데, 단 한 개의 구슬을 꺼내어 이 주머니를  좋은 구슬 주머니를 만들고 싶다. 
예를 들어, 구슬 주머니에 [8, 3, 5, 2]라는 번호가 써진 구슬이 들어있다고 가정해보자. 8을 꺼내면 [3, 5, 2]가 남게 되고 2+3=5이므로 좋은 구슬 주머니가 된다. 또한, 2를 꺼내면 [8, 3, 5]가 남게 되고 3+5=8이므로 역시 좋은 구슬 주머니가 된다. 하지만 3 또는 5를 꺼내면 좋은 구슬 주머니가 될 수 없다. 따라서 좋은 구슬 주머니가 될 수 있는 경우의 수는 2가지, 가능한 각 경우는 1번째, 4번째 구슬을 꺼내는 경우이다.
구슬의 개수와 구슬에 쓰여진 숫자가 주어졌을 때 가능한 경우의 수와 그 각각의 경우를 출력하는 프로그램을 작성하라.

입력
첫째 줄에 구슬의 개수를 나타내는 정수 N이 주어진다. (단, )
둘째 줄에 구슬에 써진 번호 이 공백으로 구분되어 주어진다. (단, )

출력
첫째 줄에 좋은 구슬 주머니를 만들 수 있는 경우의 수 k를 출력한다.
둘째 줄에 몇 번째 구슬을 꺼내야 하는지 k개의 인덱스를 공백으로 구분하여 오름차순으로 출력한다. 만약 k가 0이라면 출력하지 않는다.

입/출력 예시
:
공백
:
줄바꿈
:
탭
예시 1
입력
5
25122
출력
3
145
예시 2
입력
4
8352
출력
2
14
예시 3
입력
5
21243
출력
0
예시 4
입력
3
444
출력
3
123
'''

n = int(input())
balls = list(map(int, input().split()))
balls_sum = sum(balls)
#print("n:{}, balls:{}, balls_sum:{}".format(n, balls, balls_sum))

ball_dict = {}
for i in range(len(balls)):
  if balls[i] in ball_dict:
    ball_dict[balls[i]].append(i + 1)
  else:
    ball_dict[balls[i]] = [i + 1]
#print(ball_dict)

answer_count = 0
answer_set = set()
for k in ball_dict.keys():
  r_sum = balls_sum - k
  if r_sum % 2 == 0:
    target = r_sum / 2    
    if target in ball_dict:
      if target != k:
        answer_count += len(ball_dict[k])
        answer_set.update(ball_dict[k])
      else:
        # 자기 자신일 경우, 볼이 꺼내졌기 때문에 불가  
        if len(ball_dict[k]) >= 2:
          answer_count += len(ball_dict[k])
          answer_set.update(ball_dict[k])

print(answer_count)
#print(answer_set)

answer_list = list(answer_set)
answer_list.sort()

for i in range(len(answer_list)):
  if i < len(answer_list) - 1:
    print(answer_list[i], end=' ')
  else:
    print(answer_list[i]) 
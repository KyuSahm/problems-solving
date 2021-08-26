import time

def solution(clothes):
  cloth_type = {}    # Dictionary 선언
  # cloth type별 개수 초기화
  for i in range(len(clothes)):
    cloth_type[clothes[i][1]] = 0 # 0으로 초기화
  
  # cloth type별 개수 계산
  for i in range(len(clothes)):
    cloth_type[clothes[i][1]] += 1
    #print(clothes[i][1], cloth_type[clothes[i][1]])

  answer = 1
  # cloth type별로 선택의 경우가 개수 + 1가 존재(선택하지 않는 경우까지 포함)
  for name in cloth_type.keys():
    answer *= cloth_type[name] + 1
  # 모든 타입을 선택하지 않는 경우의 수를 빼줌  
  return answer - 1

if __name__ == '__main__':
  startTime = time.time()
  a = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
  print("first solution: {}".format(solution(a)))
  a = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
  print("second solution: {}".format(solution(a)))  

  endTime = time.time()
  print("Elapsed Time: {0}".format(endTime - startTime))
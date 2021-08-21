'''
문제 설명 - N으로 표현
아래와 같이 5와 사칙연산만으로 12를 표현할 수 있습니다.

12 = 5 + 5 + (5 / 5) + (5 / 5)
12 = 55 / 5 + 5 / 5
12 = (55 + 5) / 5

5를 사용한 횟수는 각각 6,5,4 입니다. 그리고 이중 가장 작은 경우는 4입니다.
이처럼 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.

제한사항
N은 1 이상 9 이하입니다.
number는 1 이상 32,000 이하입니다.
수식에는 괄호와 사칙연산만 가능하며 나누기 연산에서 나머지는 무시합니다.
최솟값이 8보다 크면 -1을 return 합니다.
입출력 예
N	number	return
5	12	4
2	11	3
입출력 예 설명
예제 #1
문제에 나온 예와 같습니다.

예제 #2
11 = 22 / 2와 같이 2를 3번만 사용하여 표현할 수 있습니다.

출처

※ 공지 - 2020년 9월 3일 테스트케이스가 추가되었습니다.
'''
def solution(N, number):
    if number == N:
        return 1    
    
    f = [set() for _ in range(9)]
    f[1].add(N)

    for i in range(2, 9):
        result = ''
        for _ in range(i):
            result += str(N)
        f[i].add(int(result))

        for j in range(1, i):
            k = i - j
            for x in f[j]:
                for y in f[k]:
                    result = x + y
                    f[i].add(result)
                    result = x - y
                    f[i].add(result)
                    result = x * y
                    f[i].add(result)

                    if y != 0:
                        result = x // y
                        f[i].add(result)
        if number in f[i]:
            return i
    return -1

if __name__ == '__main__':
  print(solution(5, 12))
  print(solution(2, 11))
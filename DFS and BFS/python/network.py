'''
문제 설명
네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다. 예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고, 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다. 따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.

컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.

제한사항
컴퓨터의 개수 n은 1 이상 200 이하인 자연수입니다.
각 컴퓨터는 0부터 n-1인 정수로 표현합니다.
i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현합니다.
computer[i][i]는 항상 1입니다.
입출력 예
n	computers	return
3	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]	2
3	[[1, 1, 0], [1, 1, 1], [0, 1, 1]]	1
입출력 예 설명
예제 #1
아래와 같이 2개의 네트워크가 있습니다.
image0.png

예제 #2
아래와 같이 1개의 네트워크가 있습니다.
image1.png
'''
def dfs_recursive(i, computers, visited):
    #print(i, " visited")
    visited[i] = True
  
    for j in range(0, len(computers[i])):
        if j == i:
            continue
        if visited[j]:
            continue
        if computers[i][j] == 1:    
            dfs(j, computers, visited)

def dfs_stack(i, computers, visited):
    #print(i, " visited")
    stack = []
    
    visited[i] = True
    stack.append(i)
    while stack:
        j = stack[-1]
        all_visited = True
        for k in range(len(computers[j])):
            if k != j and computers[j][k] == 1 and not visited[k]:
                visited[k] = True
                stack.append(k)
                all_visited = False
        if all_visited:
            stack.pop()

def solution(n, computers):
    visited = [False] * n
    answer = 0

    for i in range(n):
        if visited[i]:
            continue
        #dfs_recursive(i, computers, visited)       
        dfs_stack(i, computers, visited)       
        answer += 1
    return answer
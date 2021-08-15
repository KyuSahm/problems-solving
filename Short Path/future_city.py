'''
미래 도시
"이것이 코딩 테스트다" p259

Case 1:
입력:
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5

출력:
3

Case 2:
입력:
4 2
1 3
2 4
3 4

출력:
-1

'''
import time
from collections import deque


def dijkstra(cities, n, f, t):
    INF = int(1e9)
    distance = [INF] * (n + 1)

    q = deque()
    q.append((0, f))  # distance: 0, city: f

    while q:
        dist, n = q.popleft()
        if distance[n] > dist:
            if n == t:
                return dist

            distance[n] = dist
            new_dist = dist + 1
            for i in cities[n]:
                if distance[i] > new_dist:
                    q.append((new_dist, i))

    return -1


def floyd_warshall(cities, n, s, k, x):
    INF = int(1e9)
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    # make zero in own city
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                graph[i][j] = 0

    for i in range(1, n + 1):
        for j in cities[i]:
            graph[i][j] = 1
            graph[j][i] = 1

    # execute floyd-warshall algorithm
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == k or j == k:
                    continue
                else:
                    graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

    if graph[s][k] == INF or graph[k][x] == INF:
        return -1
    else:
        return graph[s][k] + graph[k][x]


if __name__ == '__main__':
    n, m = map(int, input().split())

    cities = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        cities[a].append(b)
        cities[b].append(a)

    x, k = map(int, input().split())

    s_time = time.time()
    a = dijkstra(cities, n, 1, k)
    b = dijkstra(cities, n, k, x)

    if a == -1 or b == -1:
        result = -1
    else:
        result = a + b
    e_time = time.time()
    print("dijkstra result: {}, elapsed time: {}".format(result, e_time - s_time))

    s_time = time.time()
    resutl = floyd_warshall(cities, n, 1, k, x)
    e_time = time.time()
    print("floyd-warshall result: {}, elapsed time: {}".format(result, e_time - s_time))
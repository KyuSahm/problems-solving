from collections import deque

def find(maps, visited, n, m):
    offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    q = deque([(0, 0, 1)])
    while q:
        (x, y, d) = q.popleft()

        if maps[x][y] == 0 or visited[x][y]:
            continue

        if x == n - 1 and y == m - 1:
            return d
        visited[x][y] = True
        for dx, dy in offsets:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and not visited[nx][ny]:
                q.append((nx, ny, d + 1))

    return -1

if __name__ == '__main__':
    maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]

    n = len(maps)
    m = len(maps[0])

    visited = [[False] * m for _ in range(n)]

    ans = find(maps, visited, n, m)

    print(ans)
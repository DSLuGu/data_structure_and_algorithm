'''source: https://www.acmicpc.net/problem/14500'''
'''idea: '''
import sys


N, M = map(int, sys.stdin.readline().split())
BOARD = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
CHECK = [[True] * M for _ in range(N)]

dX = [-1, 0, 1, 0]
dY = [0, -1, 0, 1]

MAX_RESULT = -1


def dfs(x, y, now, cnt): # 재귀함수로 가능한 사각형
        global MAX_RESULT
        if cnt == 4: # 정사각형이 4개가 되면 최대값과 비교하고 dfs 종료
            MAX_RESULT = max(MAX_RESULT, now)
            return None
        for i in range(4):
            new_x = x + dX[i]
            new_y = y + dY[i]
            if 0 <= new_x < N and 0 <= new_y < M:
                if CHECK[new_x][new_y]:
                    CHECK[new_x][new_y] = False
                    dfs(new_x, new_y, now+BOARD[new_x][new_y], cnt+1)
                    CHECK[new_x][new_y] = True


def no_dfs(x, y): # 재귀함수로 불가능한 사각형
    center = BOARD[x][y] # 가운데 값 고정
    wings = 4 # 상하좌우 날개
    min_result = 100000

    for i in range(4):
        new_x = x + dX[i]
        new_y = y + dY[i]
        if wings == 2: return 0 # 날개가 2개면 테트로미노를 만들지 못하므로 종료
        if new_x < 0 or new_x >= N or new_y < 0 or new_y >= M: # 범위를 벗어난 경우 날개 1개 감소
            wings -= 1
            continue
        center += BOARD[new_x][new_y] # 범위를 벗어나지 않았다면 값을 더해주고 해다 값이 최소값인지 찾는다
        min_result = min(min_result, BOARD[new_x][new_y])
    # 날개가 4개의 경우 총 5개의 정사각형이므로 가장 최소값인 사각형 1개를 빼준다.
    if wings == 4: center -= min_result
    return center


for i in range(N):
    for j in range(M):
        CHECK[i][j] = False
        dfs(i, j, BOARD[i][j], 1)
        CHECK[i][j] = True

        tmp = no_dfs(i, j)
        MAX_RESULT = max(MAX_RESULT, tmp)

print(MAX_RESULT)

'''source: https://www.acmicpc.net/problem/10972'''
'''idea: '''
import sys


N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
find = False
assert N == len(arr)

for i in range(N-1, 0, -1):
    if arr[i-1] < arr[i]:
        for j in range(N-1, 0, -1):
            if arr[i-1] < arr[j]:
                arr[i-1], arr[j] = arr[j], arr[i-1]
                arr = arr[:i] + sorted(arr[i:])
                find = True
                break
    if find:
        print(*arr)
        break

if not find: print(-1)
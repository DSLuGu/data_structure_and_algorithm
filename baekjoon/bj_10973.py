'''source: https://www.acmicpc.net/problem/10973'''
'''idea: '''
import sys


N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
flag = False
i = N - 2

while i > -1:
    if arr[i] > arr[i+1]:
        flag = True
        break
    i -= 1

if flag:
    standard = arr[i]
    before = arr[:i]
    after = arr[i:]
    after.sort(reverse=True)
    after.insert(0, after.pop(after.index(standard)+1))
else:
    print(-1)
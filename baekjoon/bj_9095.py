'''source: https://www.acmicpc.net/problem/9095'''
'''idea: '''
import sys


T = int(sys.stdin.readline())
ott = [1, 2, 4]
for i in range(3, 10):
    ott.append(ott[i-3] + ott[i-2] + ott[i-1])

for _ in range(T):
    n = int(sys.stdin.readline())
    print(ott[n-1])
'''source: https://www.acmicpc.net/problem/10819'''
'''idea: '''
import sys
from itertools import permutations

N = int(sys.stdin.readline())
datas = list(map(int, sys.stdin.readline().split()))


max_v = 0
for data in permutations(datas):
    s = 0
    for j in range(N-1): s += abs(data[j] - data[j+1])
    max_v = max(max_v, s)
print(max_v)
'''source: https://www.acmicpc.net/problem/10974'''
'''idea: '''
import sys
from itertools import permutations

N = int(sys.stdin.readline())
n_lst = [i for i in range(1, N+1)]


'''방법1'''
# for numbers in list(permutations(n_lst)):
#     for num in numbers:
#         print(num, end=' ')
#     print()


'''방법2'''
def next_permutation(lst):
    n = len(lst) - 1
    i = n
    while i > 0 and lst[i-1] >= lst[i]: i -= 1
    if i == 0: return False
    j = n
    while lst[i-1] >= lst[j]: j -= 1
    lst[i-1], lst[j] = lst[j], lst[i-1]
    j = n
    while i < j:
        lst[i], lst[j] = lst[j], lst[i]
        i += 1
        j -= 1
    return True

while True:
    print(' '.join(map(str, n_lst)))
    if not next_permutation(n_lst):
        break
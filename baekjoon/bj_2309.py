import sys
from itertools import combinations


def solve(case):
    if sum(case) == 100:
        case = list(case)
        case.sort()
        for old in case: print(int(old))
        return True
    return False


def main():
    '''source: https://www.acmicpc.net/problem/6588'''
    '''idea: '''
    child = set()
    for i in range(9):
        nai = int(sys.stdin.readline())
        if nai <= 100: child.add(nai)
    
    for case in combinations(child, 7):
        if solve(case): break
    return None


if __name__ == '__main__':
    main()
    
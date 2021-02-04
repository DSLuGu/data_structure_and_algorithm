import sys


def main():
    '''source: https://www.acmicpc.net/problem/6588'''
    '''idea: '''
    e, s, m = map(int, sys.stdin.readline().split())
    year = 0
    while True:
        year += 1
        if e == 1 and s == 1 and m == 1:
            print(year)
            break
        e -= 1; s -= 1; m -= 1
        if not e: e = 15
        if not s: s = 28
        if not m: m = 19
    return None


if __name__ == '__main__':
    main()
    
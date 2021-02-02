import sys
import itertools
input = sys.stdin.readline

def gcd(a, b):
    return gcd(b, a % b) if b else a

def main():
    '''source: https://www.acmicpc.net/problem/9613'''
    T = int(input())
    
    for t in range(T):
        num_list = list(map(int, input().split()))
        num_list = num_list[1:]
        ans = 0
        for a, b in itertools.combinations(num_list, 2):
            ans += gcd(a, b)
        print(ans)
    return None


if __name__ == '__main__':
    main()

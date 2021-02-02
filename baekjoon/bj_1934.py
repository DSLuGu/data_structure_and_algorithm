def f(a, b):
    if b > a: a, b = b, a
    while b > 0: a, b = b, a%b
    return a


def main():
    '''source: https://www.acmicpc.net/problem/1934'''
    T = int(input())
    for t in range(T):
        a, b = map(int, input().split())
        print(a * b // f(a, b))

    return None


if __name__ == '__main__':
    main()
    
def f(a, b):
    if b > a:
        a, b = b, a
    while b > 0:
        c = b
        b = a % b
        a = c
    return a

def main():
    '''
    source: https://www.acmicpc.net/problem/2609
    idea: 유클리드 호제법 큰 값을 작은 값으로 나눈 값을 활용
    '''
    A, B = map(int, input().split())
    result = f(A, B)
    print(result)
    print(A * B // result)
    return None


if __name__ == '__main__':
    main()

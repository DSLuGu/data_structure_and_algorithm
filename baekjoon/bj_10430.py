def main():
    '''
    source: https://www.acmicpc.net/problem/10430
    '''
    A, B, C = map(int, input().split())
    print((A + B) % C)
    print(((A % C) + (B % C)) % C)
    print((A * B) % C)
    print(((A % C) * (B % C)) % C)
    return None


if __name__ == '__main__':
    main()
    
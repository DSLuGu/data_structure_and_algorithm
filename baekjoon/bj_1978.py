def main():
    '''source: https://www.acmicpc.net/problem/1978'''
    N = int(input())
    input_values = map(int, input().split())
    cnt = 0
    for v in input_values:
        if v == 2:
            cnt += 1
            continue
        if v % 2 == 0 or v == 1: continue
        for i in range(v-1, 1, -1):
            if v % i == 0: break
        else: cnt += 1
    else:
        print(cnt)
    return None


if __name__ == '__main__':
    main()
    
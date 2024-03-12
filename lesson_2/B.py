def main():
    # 14 test wrong answer
    n, k = map(int, input().split())

    if n == 0 or n == 1 or k <= 0:
        print(0)
        return

    arr = list(map(int, input().split()))
    result = 0

    if k >= n:
        for i in range(n):
            for j in range(i + 1, n):
                result = max(result, arr[j] - arr[i])
    else:
        for i in range(n - k):
            for j in range(i + 1, i + k + 1):
                result = max(result, arr[j] - arr[i])

    print(result)


if __name__ == '__main__':
    main()

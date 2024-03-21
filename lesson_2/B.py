def main():
    # 14 test wrong answer
    n, k = map(int, input().split())

    arr = list(map(int, input().split()))
    result = 0

    for i in range(n):
        for j in range(k + 1):
            if i + j < n:
                result = max(result, arr[i + j] - arr[i])

    print(result)


if __name__ == '__main__':
    main()

def main():
    # OK
    k = int(input())

    if k == 0:
        print(0, 0, 0, 0)
        return

    x_cords = []
    y_cords = []
    for i in range(k):
        x, y = map(int, input().split())
        x_cords.append(x)
        y_cords.append(y)

    print(min(x_cords), min(y_cords), max(x_cords), max(y_cords))


if __name__ == '__main__':
    main()

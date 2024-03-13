def main():
    # OK
    # с разбора
    l, x1, v1, x2, v2 = map(int, input().split())
    answer = float("inf")
    for rotation in range(2):
        distance = (x2 - x1 + l) % l
        v = v1 - v2  # скорость сближения
        if v < 0:
            v = -v
            distance = (-distance + l) % l
        if distance == 0:
            answer = 0
        if v != 0:
            answer = min(answer, distance / v)
        x2 = (-x2 + l) % l
        v2 = -v2

    if answer == float("inf"):
        print("NO")
    else:
        print("YES")
        print(answer)


if __name__ == '__main__':
    main()

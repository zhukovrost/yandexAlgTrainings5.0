def create_desk():
    # шахматное поле, но с окружённая -1 (пустотой)
    desk = [[-1] * 10]
    for _ in range(8):
        desk.append([-1] + [0] * 8 + [-1])
    desk.append([-1] * 10)
    return desk


def count_neighbors(desk, i, j):
    cnt = 0
    # сдвиги, на которых есть сосед
    neighbors = (-1, 0), (1, 0), (0, -1), (0, 1)
    for shift in neighbors:
        if desk[i + shift[0]][j + shift[1]] == 1:
            cnt += 1

    return cnt


def count_walls(desk, i, j):
    if desk[i][j] != 1:
        return 0
    cnt = 0
    # сдвиги, на которых есть сосед
    neighbors = (-1, 0), (1, 0), (0, -1), (0, 1)
    for shift in neighbors:
        if desk[i + shift[0]][j + shift[1]] != 1:
            cnt += 1

    return cnt


def sol_1():
    # OK
    # это решение быстрее и менее затратное по памяти
    n = int(input())
    desk = create_desk()
    result = 0
    for _ in range(n):
        i, j = map(int, input().split())
        desk[i][j] = 1  # отметим существование фигуры
        # прибавим 4 грани, которые появились и отнимем количество пропавших граней
        result += 4 - 2 * count_neighbors(desk, i, j)

    print(result)


def sol_2():
    # OK
    n = int(input())
    desk = create_desk()
    result = 0
    for _ in range(n):
        i, j = map(int, input().split())
        desk[i][j] = 1  # отметим существование фигуры

    for i in range(1, 9):
        for j in range(1, 9):
            # количество стен вокруг
            result += count_walls(desk, i, j)

    print(result)


if __name__ == '__main__':
    sol_1()

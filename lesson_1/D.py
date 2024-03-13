# https://contest.yandex.ru/contest/59539/problems/D/
def main():
    # OK
    # сложность O(n^2)
    # решение с разбора использует материалы второй лекции
    # эти материалы я применил в задаче D во втором уроке
    matrix = [[0] * 8 for _ in range(8)]  # покрываемы фигурами клетки
    is_fig = [[0] * 8 for _ in range(8)]  # координаты фигур
    rs = []  # корды ладей (row, column)
    bs = []  # корды слонов (row, column)
    # ввод
    for i in range(8):
        row = input()[:8]
        for j in range(8):
            if row[j] == "R":
                rs.append((i, j))
                is_fig[i][j] = 1
                matrix[i][j] = 1
            elif row[j] == "B":
                bs.append((i, j))
                is_fig[i][j] = 1
                matrix[i][j] = 1

    for r in rs:  # ладьи покрывают
        # по горизонтали
        for i in range(r[1] + 1, 8):  # после фигуры
            if is_fig[r[0]][i]:  # если стоит фигура, то дальше не идти (она перегораживает путь)
                break
            matrix[r[0]][i] = 1
        for i in range(r[1] - 1, -1, -1):  # перед фигурой
            if is_fig[r[0]][i]:
                break
            matrix[r[0]][i] = 1

        # по вертикали
        for i in range(r[0] + 1, 8):
            if is_fig[i][r[1]]:
                break
            matrix[i][r[1]] = 1
        for i in range(r[0] - 1, -1, -1):
            if is_fig[i][r[1]]:
                break
            matrix[i][r[1]] = 1

    for b in bs:  # слоны покрывают
        for i in range(b[0] + 1, 8):  # северно-восточная диагональ
            j = b[1] + (b[0] - i)
            if not (0 <= j < 8):  # проверка на существование координаты
                continue
            if is_fig[i][j]:  # если стоит фигура, то дальше не идти (она перегораживает путь)
                break
            matrix[i][j] = 1

        for i in range(b[0] - 1, -1, -1):  # юго-восточная диагональ
            j = b[1] + (b[0] - i)
            if not (0 <= j < 8):
                continue
            if is_fig[i][j]:
                break
            matrix[i][j] = 1

        for i in range(b[0] + 1, 8):  # северно-западная диагональ
            j = b[1] - (b[0] - i)
            if not (0 <= j < 8):
                continue
            if is_fig[i][j]:
                break
            matrix[i][j] = 1

        for i in range(b[0] - 1, -1, -1):  # юго-западная диагональ
            j = b[1] - (b[0] - i)
            if not (0 <= j < 8):
                continue
            if is_fig[i][j]:
                break
            matrix[i][j] = 1

    # подсчёт непокрытых клеток (нулей)
    cnt = 0
    for i in range(8):
        for j in range(8):
            if matrix[i][j] == 0:
                cnt += 1

    print(cnt)


if __name__ == '__main__':
    main()

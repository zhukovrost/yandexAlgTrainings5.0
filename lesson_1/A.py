# https://contest.yandex.ru/contest/59539/problems/A/
def old_main():
    # 15 успешных тестов, 16 - memory limit
    # сложность O(n)
    p, v = map(int, input().split())  # номер дерева, у которого стоит ведро Васи и
    # на сколько деревьев он может от него удаляться
    q, m = map(int, input().split())  # аналогичные данные для Маши

    colored = set()  # множество покрашенных деревьев
    for i in range(p - v, p + v + 1):
        colored.add(i)  # деревья, которые красит Вася
    for i in range(q - m, q + m + 1):
        colored.add(i)  # деревья, которые красит Маша

    print(len(colored))  # количество деревьев


def main():
    # OK
    # сложность O(1)
    p, v = map(int, input().split())  # номер дерева, у которого стоит ведро Васи и
    # на сколько деревьев он может от него удаляться
    q, m = map(int, input().split())  # аналогичные данные для Маши

    # проверяем, лежит ли один диапазон деревьев в другом
    if p - v <= q - m and p + v + 1 >= q + m + 1:
        print(2 * v + 1)
        return
    elif p - v >= q - m and p + v + 1 <= q + m + 1:
        print(2 * m + 1)
        return

    # проверяем, пересекаются ли диапазоны
    if p + v < q - m or p - v > q + m:
        print(2 * v + 2 * m + 2)
        return

    # пересекающиеся диапазоны
    if p + v < q + m:
        print(2 * v + 2 * m + 2 - (p + v - (q - m) + 1))
        return
    elif p + v > q + m:
        print(2 * v + 2 * m + 2 - (q + m - (p - v) + 1))
        return

    # если какая-то ошибка
    print(1)
    return


if __name__ == '__main__':
    main()

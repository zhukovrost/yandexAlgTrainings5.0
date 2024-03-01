# https://contest.yandex.ru/contest/59539/problems/C/
def main():
    # OK
    # сложность O(n)
    n = int(input())  # количество строк
    cnt = 0  # кол-во нажатий (ответ)
    for i in range(n):
        a = int(input())  # кал-во пробелов
        cnt += a // 4  # нажатие Tab
        a %= 4
        if a == 3:
            cnt += 2  # Tab + backspace
        else:
            cnt += a  # кол-во пробелов

    print(cnt)


if __name__ == '__main__':
    main()

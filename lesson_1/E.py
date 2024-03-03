# https://contest.yandex.ru/contest/59539/problems/E/
def find_del(num, persons):
    for i in range(10):
        # подбор делимого числа
        if (num * 10 + i) % persons == 0:
            return str(num * 10 + i)

    return "-1"


def main():
    n, k, d = map(int, input().split())

    if n < 0 or k <= 0 or d <= 0:  # крайние случаи
        print(-1)
        return
    if n == 0:
        print(0)
        return

    summary = find_del(n, k)  # первый день

    # решение в строках, тк питону так легче
    if summary != "-1":
        summary += "0" * max(0, d - 1)  # прибыль

    print(summary)


if __name__ == '__main__':
    main()

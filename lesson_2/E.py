# https://contest.yandex.ru/contest/59540/problems/E/

class Berry:
    def __init__(self, up, down, number):
        self.up = up
        self.down = down
        self.number = number
        self.index = 0

    def get_profit(self):
        # дистанция, если улитка продет вверх, а потом вниз
        return self.up - self.down

    def is_profitable(self):
        # проходит ли улитка хоть что-то за сутки
        return self.get_profit() > 0

    def __str__(self):
        # для вывода через *array
        return str(self.number)

    def set_index(self, index):
        self.index = index


def get_dist(arr):
    # на какую высоту поднимется улитка
    cnt = 0
    for i in range(len(arr) - 1):
        cnt += arr[i].get_profit()
    cnt += arr[-1].up
    return cnt


def check_efficiency(arr, berry):
    # проверка: вдруг улитка сможет подняться выше, если ягоду, которая даёт дистанцию вверх больше всех,
    # поставить в конец
    dist_1 = get_dist(arr)
    arr = arr[:berry.index] + arr[berry.index + 1:]
    arr.append(berry)
    dist_2 = get_dist(arr)
    return dist_2 > dist_1


def reset_indexes(arr):
    for i in range(len(arr)):
        arr[i].set_index(i)
    return arr


def main():
    # Wrong Answer   16 test
    # ввод
    n = int(input())

    if n == 0:
        # крайний случай
        print(0)
        return

    profitable_berries = []
    unprofitable_berries = []

    for i in range(n):
        # ввод
        ai, bi = map(int, input().split())
        new_berry = Berry(ai, bi, i + 1)
        if new_berry.is_profitable():
            profitable_berries.append(new_berry)
        else:
            unprofitable_berries.append(new_berry)

    profitable_berries.sort(key=lambda x: x.get_profit(), reverse=True)  # сначала самые профитные
    profitable_berries = reset_indexes(profitable_berries)
    unprofitable_berries.sort(key=lambda x: x.up, reverse=True)  # сначала самый высокий

    result = 0

    if len(profitable_berries) >= 2:
        most_efficient_profitable_berry = max(profitable_berries, key=lambda x: x.up)
        if check_efficiency(profitable_berries, most_efficient_profitable_berry):
            profitable_berries = (profitable_berries[:most_efficient_profitable_berry.index] +
                                  profitable_berries[most_efficient_profitable_berry.index + 1:])
            profitable_berries.append(most_efficient_profitable_berry)
            # profitable_berries = reset_indexes(profitable_berries) - необязательно

    for i in range(len(profitable_berries) - 1):
        result += profitable_berries[i].get_profit()

    if len(unprofitable_berries) > 0 and len(profitable_berries) > 0:
        # все ягоды
        result += max(profitable_berries[-1].up, profitable_berries[-1].get_profit() + unprofitable_berries[0].up)
    elif len(unprofitable_berries) > 0 and len(profitable_berries) == 0:
        # нет профитных ягод
        result += unprofitable_berries[0].up
    else:
        # только профитные ягоды
        result += profitable_berries[-1].up

    print(result)
    print(*profitable_berries, *unprofitable_berries)


if __name__ == '__main__':
    main()

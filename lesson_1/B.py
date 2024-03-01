# https://contest.yandex.ru/contest/59539/problems/B/
def main():
    # OK
    # сложность O(1)
    g1, g2 = map(int, input().split(':'))  # G1 — число мячей, забитых первой командой,
    # а G2 "— число мячей, забитых второй командой
    cur_1, cur_2 = map(int, input().split(':'))  # аналогично для 2-го матча

    l = int(input())  # 1, если первую игру первая команда провела «дома», или 2, если «в гостях»
    is_g1_guest = 0  # 1, если текущая игра в гостях для первой команды, иначе 0
    guest_goals1, guest_goals2 = 0, 0  # кол-во голов в гостях для первой команды

    # рассматриваем два случая
    if l == 1:
        guest_goals2 += g2
        guest_goals1 += cur_1
        is_g1_guest = 1
    elif l == 2:
        guest_goals1 += g1
        guest_goals2 += cur_2

    # теперь g1 и g2 - общее число голов
    g1 += cur_1
    g2 += cur_2

    if g2 - g1 < 0:  # уже победа
        print(0)
        return

    if guest_goals1 + (g2 - g1) * is_g1_guest > guest_goals2:
        # если счёт равный и кол-во голов в гостях больше у 1-ой команды
        print(g2 - g1)
    else:
        print(g2 - g1 + 1)


if __name__ == '__main__':
    main()

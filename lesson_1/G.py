def calculate(change_mode_hp, units, hp, productivity):
    rounds, enemies = 0, 0
    # 1 режим - атаковать сначала противника, потом казарму
    while hp >= change_mode_hp:
        if enemies >= units:
            return float("inf")
        hp -= units - enemies
        enemies = 0
        if hp >= 0:
            enemies += productivity
        rounds += 1
    # 2 режим - атаковать сначала казарму, потом противника
    while hp > 0:
        if units <= 0:
            return float("inf")
        if hp >= units:
            hp -= units
        else:
            enemies -= units - hp
            hp = 0
        units -= enemies
        if hp > 0:
            enemies += productivity
        rounds += 1

    # 3 режим - атаковать только противника после сноса казармы
    while enemies > 0:
        if units <= 0:
            return float("inf")
        enemies -= units
        if enemies > 0:
            units -= enemies
        rounds += 1

    return rounds


def main():
    # решение с разбора
    x = int(input())  # количество солдат на старте игры
    y = int(input())  # здоровье казармы
    p = int(input())  # производительность

    answer = float("inf")
    # поскольку у нас небольшие входные данные, можно перебрать все варианты в лоб
    for hp in range(y + 2):
        answer = min(answer, calculate(hp, x, y, p))

    if answer != float("inf"):
        print(answer)
    else:
        print(-1)


if __name__ == '__main__':
    main()

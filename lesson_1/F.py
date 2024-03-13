# https://contest.yandex.ru/contest/59539/problems/F/

def main():
    # OK
    # решение с разбора
    _ = int(input())
    arr = list(map(int, input().split()))
    state = "no_odd"
    for n in arr:
        if state == "no_odd":
            if n % 2 == 0:
                print("+", end="")
            else:
                state = "odd"
        elif state == "odd":
            if n % 2 == 0:
                print("+", end="")
                state = "even"
            else:
                print("x", end="")
        elif state == "even":
            print("x", end="")


if __name__ == '__main__':
    main()

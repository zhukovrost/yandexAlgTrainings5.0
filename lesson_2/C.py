def main():
    _ = int(input())
    ropes = list(map(int, input().split()))
    main_rope = max(ropes)
    rest = sum(ropes) - main_rope
    if rest < main_rope:
        print(main_rope - rest)
        return
    else:
        print(sum(ropes))


if __name__ == '__main__':
    main()

def main():
    f = lambda x: x + 2
    g = lambda x: abs(x)
    print(f(2))
    print(g(-6))
    print(sorted([2, -8, 5, -6, 1, -3], key=g))


if __name__ == '__main__':
    main()

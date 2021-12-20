def main():
    a = eval(input("enter a value for a: "))
    b = eval(input("enter a value for b: "))
    c = eval(input("enter a value for c: "))
    if a + b < c or a + c < b or c + b < a:
        input("they are in error")
    else:
        input("they are correct triangle sides length")


if __name__ == '__main__':
    main()

def ackerman_function(x, y):
    if x == 0:
        return y + 1
    elif y == 0:
        return ackerman_function(x - 1, 1)
    else:
        return ackerman_function(x -1, ackerman_function(x, y - 1))

def main():
    print(ackerman_function(5, 5))

if __name__ == '__main__':
    main()


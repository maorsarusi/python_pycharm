import datetime
import sys


def main():
    now_ordinary = datetime.datetime.now()
    for i in range(1, 1000000):
        sys.stdout.write('.')
        sys.stdout.flush()
    print("\n")
    after_ordinary = datetime.datetime.now()
    current_ordinary = after_ordinary - now_ordinary

    print("finish ordinary loop")

    now_jump = datetime.datetime.now()
    for i in range(1, 1000000, 2):
        sys.stdout.write('.')
        sys.stdout.flush()
    print("\n")
    after_jump = datetime.datetime.now()
    current_jump = after_jump - now_jump
    print("finish loop with jumps")

    if current_jump > current_ordinary:
        dif = current_jump - current_ordinary
        print("jump is bigger than ordinary in {} times".format(dif))
    else:
        dif = current_ordinary - current_jump
        print("ordinary is bigger than jump in {} times".format(dif))


# 0:00:00.527910
if __name__ == '__main__':
    main()

import sys

__author__ = "Maor"
# the name of the file
NAME = 1


def print_file(file_name):
    """
    function print_file gets file name and prints its content
    :param file_name: the name of the file
    :return:
    """
    with open(file_name, 'r') as file:
        for i in file:
            print(i)


def main():
    file_mame = sys.argv[NAME]
    print_file(file_mame)


if __name__ == '__main__':
    main()

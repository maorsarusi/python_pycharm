from test import my_test


def main():
    # manage the client side
    my_test.clent_sending(my_test.sys.argv[my_test.CLIENT_INPUT])
    packages = my_test.sniff(filter="host {}".format(my_test.IP_SERVER), count=1)


if __name__ == "__main__":
    main()

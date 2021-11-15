from test import my_test


def main():
    # the manage of the server
    packages = my_test.sniff(count=1)
    my_results = []

    our_packages = my_test.just_our_packages(packages)
    print(our_packages)
    my_results = my_test.manange_result(our_packages)
    for i in my_results:
        p = my_test.IP(src=my_test.IP_SERVER, dst=my_test.IP_CLIENT) / i
        my_test.send(p)


if __name__ == "__main__":
    main()

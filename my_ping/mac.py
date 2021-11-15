from scapy.all import *

mac_string = "abcdefABCDEF"


def print_dif(frames):
    mac_list = []
    for frame in frames:
        source_mac = frame[Ether].src
        if source_mac not in mac_list:
            mac_list += [source_mac]
            print(source_mac)
    return


def valid_byte(byte):
    if len(byte) != 2:
        return False
    elif byte.isdigit():
        return True
    else:
        for i in byte:
            if not i in mac_string:
                return False
    return True


def valid_mac(mac):
    mac_list = mac.split(":")
    if len(mac_list) != 8:
        return False
    for i in mac_list:
        if not valid_byte(i):
            return False
        return True


def print_id(mac):
    identifier = mac.split(":")
    return ":".join(identifier[:3])


def main():
    frames = sniff(count=10)
    for i in frames:
        print("ip: {}".format(i[Ether].src))
    print_dif(frames)
    mac = input("Enter a mac address\n")
    if valid_mac(mac):
        print("the mac is valid\n")
        print("the create identifier is: {}".format(print_id(mac)))
    else:
        print("the mac is invalid\n")


if __name__ == "__main__":
    main()

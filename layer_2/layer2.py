from scapy.all import *

PATH = r"C:\Network\work\layer_2\Layer2_Broadcast.pcap"
BROADCAST = "ff:ff:ff:ff:ff:ff"


def main():
    pcapFile = rdpcap(PATH)
    count = 1
    count_list = []
    for i in pcapFile:
        if Ether in i and i[Ether].dst == BROADCAST:
            count_list += [str(count)]
        count += 1
    print("the serial number of frames that sends to broadcast are: {}".format(", ".join(count_list)))
    return


if __name__ == "__main__":
    main()

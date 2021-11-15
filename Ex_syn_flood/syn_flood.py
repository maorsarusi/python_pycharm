from scapy.all import *

# const values to the program
PATH_WIRESHARK = r"C:\Network\work\Ex_syn_flood\SynFloodSample.pcap"
IP_ATTACKERS_FILE = r"C:\Network\work\Ex_syn_flood\ip_attackers.txt"
SYN = 0x02
ACK = 0x10
SYN_ACK = 0x12
# בחרתי ב 5 כי לדעתי מי ששולח הרבה syn ללא  ack
# ייחשב כתוקף רק אם זה מעל 5 כי אולי הוא מזהה שלא קיבל syn ack לכן הוא שולח שוב
# כמו"כ גם מי שקיבל syn ack  ולא החזיר  ack נחשב כתוקף מבחינתי
LIMIT_TO_ATTACKERS = 5


def list_src(pcapFile):
    """
    function list_src gets a pcap file and extract from it the ip's of all sources
    :param pcapFile: the file from wireshark
    :return:  a list with all ip sources
    """
    ip_list = []
    for packet in pcapFile:
        src = packet[IP].src
        if src not in ip_list:
            ip_list += [packet[IP].src]
    return ip_list


def create_dictionary(some_list):
    """
    function create_dictionary gets a list and create a dictionary to count for every key
    :param some_list:  the list that will be the keys in the dictionary
    :return:            a dictionary with values like this {ip:0}
    """
    zero_list = [0] * len(some_list)
    dictionary = dict((zip(some_list, zero_list)))
    return dictionary


def count_syn(ip_dictionary, pcap_list):
    """
    function count_syn counts for every ip source the number of syns it sends
    :param ip_dictionary: the dictionary to count the syns
    :param pcap_list: the list of packets to check the sources
    :return: the update dictionary with the ip's and the number of syns it sends
    """
    for pkt in pcap_list:
        if pkt[TCP].flags == SYN:
            ip = pkt[IP].src
            ip_dictionary[ip] += 1
    return ip_dictionary


def sub_acks(ip_dict, pcap_list):
    """
    function sub_acks count the relation between syn to acks for every ip address that appears in the dictionary
    :param ip_dict: the dictionary of ip's
    :param pcap_list:  the list of packets to check the sources
    :return: the update dictionry with the ip's and the relation between syns to acks that it sends
    """
    for pkt in pcap_list:
        if pkt[TCP].flags == ACK:
            ip = pkt[IP].src
            ip_dict[ip] -= 1
    return ip_dict


def no_ack_after_sa(pcap_file):
    """
    function no_ack_after_sa gets a pcap file and search for all the ip's
    that gets a syn ack message and don't reply ack
    :param pcap_file: the file from wireshark
    :return: a list with all the ip's  that gets a syn ack message and don't reply ack
    """
    no_ack_list = []
    for pkt in pcap_file:
        if pkt[TCP].flags == SYN_ACK:
            ip = pkt[IP].dst
            no_ack_list += [ip]
    for pkt in pcap_file:
        if pkt[TCP].flags == ACK and pkt[IP].src in no_ack_list:
            no_ack_list.remove(pkt[IP].src)
    return no_ack_list


def write_attackers(ip_dict, no_response_ack):
    """
     function write_attackers write to a file the ip's of every device who sends a lot of syns and to return enough acks
     or gets a syn ack response and don't reply ack
    :param ip_dict: the update dictionary
    :param no_response_ack: the list of the ip's  that gets a syn ack response and don't reply ack
    """
    written = []
    for ip in ip_dict.keys():
        if ip_dict[ip] > LIMIT_TO_ATTACKERS:
            written += [ip]
    for ip in no_response_ack:
        if ip not in written:
            written += [ip]
    with open(IP_ATTACKERS_FILE, "w") as file:
        file.write("the attackers ip:\n")
        for ip in written:
            file.write("{}\n".format(ip))


def main():
    pcapFile = rdpcap(PATH_WIRESHARK)

    # start to create the ip dictionary
    src_list = list_src(pcapFile)
    ip_dict = create_dictionary(src_list)

    # calculate the relation between syns and acks for the ip's
    ip_dict = count_syn(ip_dict, pcapFile)
    ip_dict = sub_acks(ip_dict, pcapFile)

    # find the other attackers and write them all
    no_response_ack = no_ack_after_sa(pcapFile)
    write_attackers(ip_dict, no_response_ack)
    print("the attackers written in the file\n")
    return


if __name__ == "__main__":
    main()

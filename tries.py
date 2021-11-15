def events(event_list):
    bin_list = []
    for event in event_list:
        bin_event = bin(event)[2:]
        bin_list += [("0" * (32 - len(bin_event)) + bin_event)[::-1]]
    bin_string = "".join(bin_list)
    return [j for j in range(len(bin_string)) if bin_string[j] == '1']


def main():
    event_state = [1020, 524352, 0, 268435456, 0, 10485760, 802824, 3584, 0, 0]
    print(events(event_state))
    x = []
    z = []
    r = []
    nums = [i for i in range(10)]
    for i in nums:
        for j in nums:
            for k in nums:
                for l in nums:
                    x = [str(i), str(j), str(k), str(l)]
                    z = [str(l), str(k), str(j), str(i)]
                    x = "".join(x)
                    z = "".join(z)
                    if int(x) * 0 == int(z):
                        r += [x]
    print(r)


if __name__ == "__main__":
    main()

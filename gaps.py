# סעיף א'
def gap_single(s, ch):
    places = [i for i in range(len(s)) if s[i] == ch]  # can be converted to a regular loop
    if len(places) == 0:
        return ch, None, None
    elif len(places) == 1:
        return ch, places[0], -1
    first_appearance = places[0]
    last_appearance = places[-1]
    return ch, first_appearance, last_appearance - first_appearance


# סעיף ב'
def gap_avg(s):
    d = {}
    appearance = 0
    sum = 0
    for i in range(len(s)):
        if not s[i] in d.keys():
            d[s[i]] = [i, -1]
        else:
            appearance = i
            d[s[i]][1] = appearance - d[s[i]][0]
    for k in d.keys():
        sum += d[k][1]
    return sum / len(d.keys())


# סעיף ג'
def get_str_len(si):
    length = 0
    for i in si:
        if i[1] > length:
            length = i[1]
        if i[2] != -1 and (i[1] + i[2]) > length:
            length = i[1] + i[2]
    return length


def restore_str(li):
    length = get_str_len(li)
    arr = ["0"] * (length + 1)
    for i in li:
        first = i[1]
        arr[first] = i[0]
        if i[2] != -1:
            last = i[2]
            arr[first + last] = i[0]
    return "".join(arr)

    return arr

# סעיף ד
def li_of_append(li1, li2):
    small_length = len(li1)
    if len(li2) < small_length:
        small_length = len(li2)
    for i in range(small_length):
        if li1[i][0] in li2:
            if


def main():
    s1 = "mabracadabra"
    li = [['m', 0, -1],
          ['a', 1, 10],
          ['b', 2, 7],
          ['r', 3, 7],
          ['c', 5, -1],
          ['d', 7, -1]]
    for c in ['m', 'a', 'b', 'r', 'c', 'd']:
        print(gap_single(s1, c))
    print(gap_avg(s1))
    print(get_str_len(li))
    print(restore_str(li))


if __name__ == "__main__":
    main()

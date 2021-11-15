ELBIT = r"C:\Network\work\elbitsystems.elbit"


def zfill_bin(binary):
    if len(binary) == 4:
        return binary
    if len(binary) < 4:
        binary = "0" * (4 - len(binary)) + binary
        return binary
    else:
        binary1 = binary[0:len(binary) % 4]
    return zfill_bin(binary1) + binary[len(binary) % 4:]


def reverse_bin(binary):
    return binary[::-1]


def from_bin_to_hex(binary):
    binary = zfill_bin(binary)
    reverse_binary = reverse_bin(binary)
    list_bin = []
    for i in range(0,len(reverse_binary),4):
        list_bin += reverse_binary[i:i+4]
        list_bin += [" "]
    return "".join(list_bin).split(" ")


index = 203
l = []
l1 = []
l2 = []
with open(ELBIT, "rb") as file:
    for i in file:
        l2 += [i]
        l += [i.decode("utf-8", "ignore")]

l1 = l[203:]
l2 = ""
for i in l1:
    if i == ",":
        break
    else:
        l2 += str(i)
# print(len(l2))
# for i in range(len(l2)-3):
#  print(str(ord(l2[i:i+1])))

binary = bin(36)[2:]
# print(l1)
# print(l2[203:])
print(binary)
x = zfill_bin(binary)
print(x)
y = reverse_bin(x)
print(y)
print(from_bin_to_hex(binary))

import random

PATH_USED = r"C:\Network\work\english\used.txt"


def main():
    cap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    small = "abcdefghijklmnopqrstuvwxyz"
    used = []
    count = 0
    deleting = input("האם אתה רוצה למחוק את הקובץ כן/לא?" + "\n")
    if deleting != "כן" and deleting != "לא":
        print("שגיאה בהכנסה. ברירת המחדל היא שהקובץ לא יימחק" + "\n")
    else:
        if deleting == "כן":
            f = open(PATH_USED, "r+")
            f.truncate()
            with open(PATH_USED, "w") as f:
                f.write("used data:\n")

    while True:
        rand = random.randint(0, len(cap) - 1)
        print("האות שהוגרלה:")
        random_letter = cap[rand]
        with open(PATH_USED, "r") as f:
            for i in f:
                used += [i[0]]
        used = used[1:]
        while random_letter in used:
            rand = random.randint(0, len(cap) - 1)
            random_letter = cap[rand]
        print(random_letter)
        count += 1
        with open(PATH_USED, "a")as f:
            f.write(random_letter + "\n")
        if count == len(cap):
            break
        y = input("להראות את האות הקטנה?" + "\n")
        while True:
            if y == "y":
                print(small[rand])
                break
            y = input()
        x = input("להמשיך?" + "\n")
        if x == "n":
            break


if __name__ == "__main__":
    main()

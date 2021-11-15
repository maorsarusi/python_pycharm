from mathematics import Dice
import  random

PATH =  r"C:\Network\work\mathematics\exercisesAll.txt"
def main():
    r = [i for i in range(136)]
    ex = []
    result = []
    l = []
    with open(PATH, "r") as f:
        for i in f:
           l = i.split("=")
           ex += [l[0]]
           result += [l[1][1:-1]]
    print(result)
    tardic = dict(zip(result, ex))
    print(tardic)
    while True:
        d1 = Dice.Dice(1)
        d2 = Dice.Dice(2)
        print(d1)
        print(d2)
        num1 = d1.get_number()
        num2 = d2.get_number()
        print("ביחד:{}".format(num1 + num2))
        if num1 == num2:
            print("תור נוסוף, במידה ויוצא עוד דאבל תיאלץ לחזור אחורה")
            x = input("זרוק שוב{}".format("\n"))
            d1 = Dice.Dice(1)
            d2 = Dice.Dice(2)
            print(d1)
            print(d2)
            num1 = d1.get_number()
            num2 = d2.get_number()
            print("ביחד:{}".format(num1 + num2))
            if num1 == num2:
                print("יש לחזור אחורה {} צעדים{}".format("\n", num1))
        con = input("להמשיך?{}".format("\n"))
        if con == "n":
            break
        ask = input("האם יש נחש או סולם?{}".format("\n"))
        if ask == "y":
                x = random.randint(0, 135)
                s = result[x]
                print(tardic[s])
                input("תוצאה{}".format("\n"))
                print(s)






if __name__ == "__main__":
    main()

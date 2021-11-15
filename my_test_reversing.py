def check(user_input):
    length = len(user_input[1:])# בגלל שהכנסנו בראש 0
    if length <= 3:
        return
    else:
         x = 0x0
         for i in user_input[1:]:
             o = ord(i)
             y = bin(0)
             z = str(x[2:])# כביכול עוזר לי להגיע לביטים
             for j in z:
                 if int(z) == 1:
                     x += 0x1
                 z = z[0:-2]
         if x == 0x15:
           print("Great!")




def main():
    user_input = input("Enter Password\n") # שורה זו מדמה את ההדפסה של המחרוזת על המסך וכמו"כ את קבלת הקלט מהמשתמש
    check("0" + user_input)# הדימוי הכי טוב שהיה לי בשביל להגיד שהbyte הראדון הוא 0

if __name__ == "__main__":
    main()
class CalculateAndTrack:
    # איתחול כמו שביקשו בתרגיל
    def __init__(self, start_date, end_date, table):
        self.__start_date = start_date
        self.__end_date = end_date
        self.__table = table
        self.__track = dict()

    def __repr__(self):
        dates = "start:{}, end:{} ".format(self.__start_date, self.__end_date)
        details = ""
        tables_key = self.__table.keys() # מקבל את כל המפתחות בtable
        for key in tables_key:
          if key in self.__track.keys():# בדיקה אם המפתח נמצא בtrack כלומר אם עשינו מערב כבר על איזור זה
            d = self.__track[key] # מקבל את הפרטים (רשימש של מספר הבקשות וסכום ההחזרים)
            details += "area: {} num of requests: {}, num of returns: {}\n".format(key, d[0], d[1])
        return dates + details

    def money_return(self, pName, zone, bottles1, bottles2):
        if  zone not in self.__track.keys(): # בודק אם האיזור נבדק
            self.__track[zone] = [0, 0] # אם לא נבדק מאפס את ערכי המעקב
        self.__track[zone][0] += 1 # מוסיף אחד לאיזור הבקושת
        pikadons = self.__table[zone] # מקבל את ערך הפיקדונות עבור איזור לפי  הפונקציה מסעיף א
        pBottels1 = pikadons[0] * bottles1 # מחשב פיקדון א'
        pBottels2 = pikadons[1] * bottles2 # מחשב פיקדון ב'
        sum_pikadons = pBottels1 + pBottels2 # מחשב סכום פקדונות
        self.__track[zone][1] += sum_pikadons # מוסיף את סכום הפקדונות לסכום הפקדונות הקודם
        return tuple([pName, sum_pikadons]) # יוצר רשומה של מבקש הבקשה והסכום הכללי שמגיע לו


def get_table(file_name):
    cities = []
    prices = []
    with open(file_name, 'r') as f:
        for line in f:
            save = line.split(",") # מפצל את הטקסט לפי , ככה שיהיה לנו רשימה שתיראה כך לדוג'[3, 4,"jerusalem"]
            cities.append(save[0]) # מכניס לרשימה את שמות הערים
            # את שתי השורות האלה הוספתי כי מקבלים גם את התו של ירידת שורה וזה מוריד אותו
            price_a = float(save[1]) # יוצר את פיקדון א כמספר
            price_b = float(save[2]) # יוצר את פיקדון ב כמספר
            prices.append(tuple([price_a, price_b])) # יצירת רשומה של שני הפקדונות
    return dict(zip(cities, prices)) # יצירת מילון עם 2 הרשימות

def main():
    x = get_table(r"cities_file.txt")
    print(x)
    tracker = CalculateAndTrack("1.1.21", "1.2.21",x)
    print(tracker.money_return("tal", "Jerusalem", 4, 5))
    print(tracker.money_return("tal", "Jerusalem", 4, 5))
    print(tracker.money_return("tal", "Tel Aviv", 4, 5))
    print(tracker.__repr__())


if __name__ == "__main__":
    main()

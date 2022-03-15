import csv
import os

"""
represents the israeli coins
"""
shekels = '₪'


class product:
    """
    class product represent a product in the shop
    """

    def __init__(self, line, name, buy_price, selling_price, amount_buy, num_of_sell):
        if amount_buy == '':
            amount_buy = 0
        if buy_price == '':
            buy_price = 0
        if num_of_sell == '':
            num_of_sell = 0
        if selling_price == '':
            selling_price = 0

        self.__line = line
        self.__name = name
        self.__amount_buy = amount_buy
        self.__price = buy_price
        if shekels not in buy_price:
            add_shekel(buy_price)
        self.__selling_price = selling_price
        if shekels not in selling_price:
            self.__selling_price = add_shekel(self.__selling_price)
        self.__num_of_sell = num_of_sell

        self.__earning = add_shekel(str(extract_number(num_of_sell) * extract_number(selling_price) - extract_number(
            amount_buy) * extract_number(buy_price)))

    def set_amount_buy(self, amount):
        """
        a method to set the product's amount
        :param amount: the number of buying products
        """
        self.__amount_buy = amount

    def set_price(self, price):
        """
        a method to set the price of the product
        :param price: the price of the product
        """
        self.__price = price

    def set_selling_price(self, selling_price):
        """
        a method to set the selling price of a product
        :param selling_price: the price we sell the product
        """
        self.__selling_price = selling_price

    def set_num_of_sell(self, num):
        """
        a method that set the number of products we sell
        :param num: the number of prosucts to set
        """
        self.__num_of_sell = num

    def set_name(self, name):
        """
        a method that set the name of the product
        :param name: the new name of the product
        """
        self.__name = name

    def set_line(self, line):
        """
        a method that set the number of the line of product in the vcs file
        :param line: the number to set
        :return:
        """
        self.__line = line

    def set_earning(self):
        """
        a method to set (calculate) the earning of the product
        """
        self.__earning = extract_number(self.get_num_of_sell()) * extract_number(
            self.get_selling_price()) - extract_number(self.get_num_of_buy()) * extract_number(self.get_buy_price())

    def get_name(self):
        """
        a method to get the name of the product
        :return: the product's name
        """
        return self.__name

    def get_earning(self):
        """
        a method to get the earning of the product
        :return: the product's earning
        """
        return self.__earning

    def get_line(self):
        """
        a method to get the line of the product in the csv file
        :return: the product's line in the csv file
        """
        return self.__line

    def get_buy_price(self):
        """
        a method to get the price that we bought the product
        :return: the product's buy price
        """
        return self.__price

    def get_selling_price(self):
        """
        a method to get the price we want to sell the product
        :return: the product's selling price
        """
        return self.__selling_price

    def get_num_of_sell(self):
        """
        a method to get the number of products we sell from a specific product
        :return: the number of selling from some product
        """
        return self.__num_of_sell

    def get_num_of_buy(self):
        """
        a method to get the number of products we bought from a specific product
        :return: the number of buying from some product

        """
        return self.__amount_buy

    def print_product(self):
        """
        a method to print by order the product's details
        """
        return str(self.get_earning()) + " רווח: "[::-1] + ',' + str(self.get_num_of_buy()) + " מספר פריטים שנקנו: "[
                                                                                              ::-1] + ',' + str(
            self.get_num_of_sell()) + " מספר פריטים שנמכרו: "[
                                      ::-1] + ',' + str(self.get_selling_price()) + " מחיר מכירה: "[
                                                                                    ::-1] + ',' + str(
            self.get_buy_price()) + " מחיר קנייה: "[::-1] + ',' + self.get_name()[::-1] + " (" + str(self.get_line())

    def print_earning(self):
        return "{}) {} : {} shekels".format(self.get_line(), self.get_name(), self.get_earning())


def extract_number(string):
    """
    a function to get a number represent by string with a shekel and get the number only
    :param string: the string we got
    :return: the number in float type
    """
    if shekels in string:
        return float(string[2:])
    else:
        return float(string)


def read_file():
    """
   a function to manage the file to a lists so we can use the details
    :return: a tuple of two lists and one string:
             1) the data of the file by lines
             2) the products by objects
             3) the path of the file
    """
    product_list = []
    fixed_lines = []
    path = input("הכנס רק את שם הקובץ אותו תרצו לקרוא"[::-1] + "\n")
    all_path = path + '.csv'
    while True:
        if os.path.exists(all_path):
            with open(all_path, 'r') as csv_file:
                lines = csv.reader(csv_file)
                data_with_header = list(lines)
            data = data_with_header[1:]  # the whole data without the titles
            header = data_with_header[0]  # the titles
            for line in data:
                fixed_lines += [insert_zeros(line)]  # insert to places of prices zero if they are empty
            for i in fixed_lines:
                p = product(i[0], i[1], i[2], i[3], i[4], i[5])  # create an object of product
                product_list += [p]
            fixed_lines.insert(0, header)
            break
        else:
            all_path = input("אין קובץ כזה נסו שנית"[::-1] + "\n") + '.csv'

    return fixed_lines, product_list, all_path


def insert_zeros(line):
    """
    a function that inserts to an empty place un a specific line a zero
    :param line: the line to insert the zeros
    :return: the new line with the zeros
    """
    for i in range(len(line)):
        if line[i] == '':
            line[i] = '0'
    return line


def write_new_file(file):
    """
    a function to write a copy to a file
    :param file: the file to copy
    """
    name = "שקל וחצי פלוס "
    name += input("הכנס את שם הקובץ הרצוי"[::-1] + "\n")  # the file name will be "שקל וחצי פלוס" + the name wr gave
    whole_name = "{}.csv".format(name)
    if os.path.exists(whole_name):
        print("שם לא קיים"[::-1] + '\n')
        return
    with open(whole_name, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(file)
    name = name[::-1]
    print("רצונ {} ץבוק".format("{}.csv".format(name)))


def move_lines(file, products, num):
    """
    a private function to arrange the lines of product after a product has been deleted
    :param file: the file we have in list of lists
    :param products: the file in list of products
    :param num: the number of the line we need to delete
    :return: the new file and products arranged by the new order after the deleting
    """
    for prod in products[num - 1:]:  # the products form the wanted to delete product down in product list
        prod.set_line(int(prod.get_line()) - 1)
    for prod in file[num:]:  # the products form the wanted to delete product down in file list
        prod[0] = str(int(prod[0]) - 1)
    return file, products


def find_how_many_times(character, string):
    """
    a private function to find how many times a character appears in a string
    :param character: the character to find
    :param string: the string to search in
    :return: a list with the all places that's the character appears in the string
    """
    return [i for i in range(len(string)) if string[i] == character]


def check_float_int(string):
    """
    a function to check if a string is an int or a float(double)
    :param string: the string we check
    :return: -1 if it isn't a float or an int
              0 if it an int
              1 if it a float
    """
    if '.' not in string:  # can't be a float
        for character in string:
            if not character.isdigit():  # isn't an int either
                return -1
        return 0  # it's an int
    else:
        dots = find_how_many_times('.', string)
        if len(dots) > 1:  # means that it isn't a float
            return -1
        else:
            new_string = string[0:dots[0]] + string[dots[0] + 1:]  # check the parts from the dot and to the dot
            for character in new_string:
                if not character.isdigit():
                    return -1
            return 1  # means that it's a float


def add_line(file, products):
    """
    a function to add a product to the file
    :param file: the file we have in list of lists
    :param products: the file in list of product
    :return: the new file and products with the new line
    """
    length = str(len(file))
    name = input("הכנס שם מוצר"[::-1] + "\n")
    buy = input("הכנס מחיר קנייה"[::-1] + "\n")
    while check_float_int(buy) == -1:
        print("הכנסתם ערך לא טוב נסו שנית"[::-1] + "\n")
        buy = input("הכנס מחיר קנייה"[::-1] + "\n")
    sell = input("הכנס מחיר מכירה"[::-1] + "\n")
    while check_float_int(sell) == -1:
        print("הכנסתם ערך לא טוב נסו שנית"[::-1] + "\n")
        sell = input("הכנס מחיר מכירה"[::-1] + "\n")
    num_buy = input("הכנס מספר פריטים שנקנו"[::-1] + "\n")
    while check_float_int(num_buy) == -1:
        print("הכנסתם ערך לא טוב נסו שנית"[::-1] + "\n")
        num_buy = input("הכנס מספר פריטים שנקנו"[::-1] + "\n")
    num_sell = '0'
    p = product(length, name, buy, sell, num_buy, num_sell)
    products += [p]
    earning = p.get_earning()  # calculate and add the earning for the new line
    line = [length, name, buy, sell, num_buy, num_sell, earning]
    file += [line]
    file = insert_shekels(file)

    return file, products


def add_shekel(string):
    """
    a private function to add the sign "shekel" in the string
    :param string: the string we add to it the sign
    :return: the new string with the sign "shekel" in it
    """
    return "{} {}".format(shekels, string)


def change_line(products, file, line_num):
    """
    a function to change a specific line in any parameter in it
    :param file: the file we have in list of lists
    :param products: the file in list of product
    :param line_num: the line we change
    :return: the new file and products with the changed line

    """
    p = None
    for prod in products:
        # find the product represented by the line
        line = prod.get_line()
        if line == str(line_num):
            p = prod
            break
    if p is None:
        print("אין שורה כזו"[::-1] + "\n")
        return
    else:
        part = input("מה תירצו לשנות?"[::-1] + "\n" +
                     "שם מוצר הקישו 1"[::-1] + "\n" +
                     "מחיר קנייה הקישו 2"[::-1] + "\n" +
                     "מחיר מכירה הקישו 3"[::-1] + "\n" +
                     "מספר פריטים שנקנו הקישו 4"[::-1] + "\n" +
                     "מספר פריטים שנמכרו הקישו 5"[::-1] + "\n" +
                     "לצאת הקישו 0"[::-1] + "\n")
        while True:
            if part == '0':
                break
            elif part == '1':
                name = input("הכנס שם חדש"[::-1] + "\n")
                p.set_name(name)
                file[line_num][1] = name
            elif part == '2':
                buy = input("הכנס מחיר קנייה חדש"[::-1] + "\n")
                while check_float_int(buy) == -1:
                    print("הערך לא טוב נסו שנית"[::-1] + "\n")
                    buy = input("הכנס מחיר קנייה חדש"[::-1] + "\n")
                p.set_price(buy)
                file[line_num][2] = add_shekel(buy)
            elif part == '3':
                sell = input("הכנס מחיר מכירה חדש"[::-1] + "\n")
                while check_float_int(sell) == -1:
                    print("הערך לא טוב נסו שנית"[::-1] + "\n")
                    sell = input("הכנס מחיר מכירה חדש"[::-1] + "\n")
                p.set_selling_price(sell)
                file[line_num][3] = add_shekel(sell)
            elif part == '4':
                num = input("הכנס מספר פריטים שנקנו"[::-1] + "\n")
                while check_float_int(num) == -1:
                    print("הערך לא טוב נסו שנית"[::-1] + "\n")
                    num = input("הכנס מספר פריטים שנקנו"[::-1] + "\n")
                p.set_amount_buy(num)
                file[line_num][4] = num
            elif part == '5':
                num = input("הכנס מספר פריטים שנמכרו"[::-1] + "\n")
                while check_float_int(num) == -1:
                    print("הערך לא טוב נסו שנית"[::-1] + "\n")
                    num = input("הכנס מספר פריטים שנמכרו"[::-1] + "\n")
                while int(num) > int(p.get_num_of_buy()):
                    print("מספר הפריטים שנקנו קטן ממספר הפריטים שנמכרו וזה לא טוב"[::-1] + "\n")
                    num = input("הכנס מספר פריטים שנמכרו"[::-1] + "\n")
                p.set_num_of_sell(num)
                file[line_num][5] = num
            else:
                print("מספר לא נכון"[::-1] + "\n")
            part = input("מה תירצו לשנות?"[::-1] + "\n" +
                         "שם מוצר הקישו 1"[::-1] + "\n" +
                         "מחיר קנייה הקישו 2"[::-1] + "\n" +
                         "מחיר מכירה הקישו 3"[::-1] + "\n" +
                         "מספר פריטים שנקנו הקישו 4"[::-1] + "\n" +
                         "מספר פריטים שנמכרו הקישו 5"[::-1] + "\n" +
                         "לצאת הקישו 0"[::-1] + "\n")
        p.set_earning()
        file[line_num][6] = add_shekel(p.get_earning())
        products[line_num - 1] = p
        return file, products


def add_earning(file, products, path):
    """
    a function to add the earning for a product
     :param file: the file we have in list of lists
    :param products: the file in list of product
    :param path: the path of the file
    :return: the new file and products with the earning parameter
    """
    for i in range(len(products)):
        if len(file[i + 1]) != 7:  # it means we haven't the earning parameter for this product
            file[i + 1].append(products[i].get_earning())
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(file)
    return file, products


def deleting_line(file, products, line_num):
    """
    a function to delete a specific product
       :param file: the file we have in list of lists
    :param products: the file in list of product
    :param line_num: the line we change
    :return: the new file and products without the deleting line
    """
    length = len(products)

    # checks if we insert a wrong number
    if length < line_num:
        print("יש רק {} שורות".format(str(length)[::-1])[::-1] + '\n')
    elif line_num < 1:
        print("{}אפשר להתחיל רק מ 1".format("\n"))
    else:
        file.pop(line_num)
        products.pop(line_num - 1)
        file, products = move_lines(file, products, line_num)
        print(" נמחקה בהצלחה "[::-1] + str(line_num) + " שורה מספר: "[::-1] + "\n")
    return file, products


def delete_file(path):
    """
    a function to delete a whole file
    :param path: the path of the deleting file
    """
    insurance = input(
        " האם אתם בטוחים? למחיקת קובץ הקישו y ליציאה הקישו כל דבר )שימו לב במחיקה שאתם על אנגלית כי זה לא ימחק אם תרשמו ט("[
        ::-1] + "\n")
    if insurance != 'y':
        print("בחרתם לצאת בלי למחוק"[::-1] + "\n")
        return
    os.remove(path)
    name = path.split(".")[0]
    print("קובץ {} נמחק".format(name[::-1])[::-1])


def insert_shekels(file):
    """
    a function to insert the symbol "shekel" if it didn't appear where it needed
    :param file: the file we check
    :return: the corrected file
    """
    for i in range(1, len(file)):
        if shekels not in file[i][2]:  # buy
            file[i][2] = shekels + " " + file[i][2]
        if shekels not in file[i][3]:  # sell
            file[i][3] = shekels + " " + file[i][3]
        if len(file[i]) == 7:
            if shekels not in file[i][6]:  # earning
                file[i][6] = shekels + " " + file[i][6]
    return file


def print_file(products):
    """
    a function to print a file
    :param products: the file in list of product
    """
    for p in products:
        print('{}'.format(p.print_product().rjust(10)))


def main():
    file, products, path = read_file()  # gets the file by lists and products and its path
    file = insert_shekels(file)
    file, products = add_earning(file, products, path)

    while True:
        operation = input("{}הקש מספר פעולה".format("\n")[::-1] +
                          "{}ליציאה הקש 0".format("\n")[::-1] +
                          "{}להעתיק את הקובץ לקובץ נוסף הקש 1".format("\n")[::-1] +
                          "{}להוסיף שורה הקש 2".format("\n")[::-1] +
                          "{}לשנות שורה הקש 3".format("\n")[::-1] +
                          '{}למחוק שורה הקש 4'.format("\n")[::-1] +
                          "{}להדפיס שורה כלשהי הקש 5".format("\n")[::-1] +
                          "{}למחוק את הקובץ הקש 6".format("\n")[::-1] +
                          "{}להדפיס את הקובץ הקש 7".format("\n")[::-1])
        if operation == '0':  # exit
            break
        elif operation == '1':  # copy file
            write_new_file(file)
        elif operation == '2':  # add line
            file, products = add_line(file, products)
            with open(path, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(file)
        elif operation == '3':  # change line
            num = input("{}הכנס מספר שורה שתרצו לשנות".format("\n")[::-1])
            print_num = int(num)
            while print_num > len(products) or print_num < 1:
                print("{}שורה לא קיימת".format("\n")[::-1])
                num = input("{}הכנס מספר שורה שתרצו לשנות".format("\n")[::-1])
                print_num = int(num)
            print(products[print_num - 1].print_product())
            file, products = change_line(products, file, print_num)
            print(products[print_num - 1].print_product())
            with open(path, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(file)
        elif operation == '4':  # deleting line
            operation = input("{}הכניסו מספר שורה שתרצו למחוק".format("\n")[::-1])
            while check_float_int(operation) != 0:
                print("{}טעות בהקלדה".format("\n")[::-1])
                operation = input("{}הכניסו מספר שורה שתרצו למחוק".format("\n")[::-1])
            file, products = deleting_line(file, products, int(operation))
            with open(path, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(file)
        elif operation == '5':  # show one line
            line = int(input("{}הכניסו מספר שורה אותה תרצו לראות".format("\n")[::-1]))
            while line > len(products) or line < 1:
                line = int(input("{}שורה לא קיימת נסו שוב".format("\n")[::-1]))
            print(products[line - 1].print_product())
        elif operation == '6':  # deleting file
            delete_file(path)
        elif operation == '7':  # print file
            print_file(products)
        else:
            print("{}לא טוב בשביל התפריט, נסו שוב".format("\n")[::-1])


if __name__ == '__main__':
    main()

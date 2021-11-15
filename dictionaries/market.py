from dictionaries import dictionary
import os

SHOP_FILE = "shop.txt"



def main():
    prod_list = []
    price_list = []
    if os.path.exists(SHOP_FILE):
        exist_dic = list(dictionary.from_file_to_dict(SHOP_FILE))
    else:
        exist_dic = {}
    while True:
        op = input(
            "do tou want to add any product or to delete?\npress 1 to add and 2 to delete to exit insert something\n")
        if op == "1":
            product = input("insert a product\n")
            if os.path.exists(SHOP_FILE) and (not dictionary.check_product(SHOP_FILE, product) or product in exist_dic):
                answer = input("The product is already exist, do you want to change it's cost? press y/n\n")
                if answer == "y":
                    price = input("insert the price to change\n")
                    dictionary.change_price(product, price, SHOP_FILE)
                    if product in prod_list:
                        price_list = dictionary.minus_num(price_list, prod_list.index(product))
                        prod_list = dictionary.minus_prod(prod_list, product)

            else:
                price = input("and its price\n")
                if product not in exist_dic:
                    prod_list += [product]
                    price_list += [float(price)]
            exist_dic += [product]
        elif op == '2':
            product = input("Insert the product you want to remove\n")
            prod_list, price_list = dictionary.delete_product(SHOP_FILE, product, prod_list, price_list)
        else:
            break

    shop = dictionary.create_dictionary(prod_list, price_list)
    dictionary.create_file(shop, SHOP_FILE, dictionary.COST, dictionary.APPEND)
    print(dictionary.print_product(SHOP_FILE))


if __name__ == "__main__":
    main()

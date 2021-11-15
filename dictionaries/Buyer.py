from dictionaries import dictionary
from dictionaries import market

BUYER_FILE = "buyer receive.txt"


def main():
    prod_list = []
    amount_list = []
    shop = dictionary.from_file_to_dict(market.SHOP_FILE)
    while True:
        product = input("Insert the product you want to buy, for finish insert 0\n")
        if product == '0':
            break
        elif product not in shop:
            print("this product isn't exist\n")
        else:
            amount = input("insert the amount (kg or how many) you want to buy\n")
            prod_list += [product]
            amount_list += [float(amount)]
    buyer = dictionary.create_dictionary(prod_list, amount_list)
    dictionary.recieve(buyer, BUYER_FILE)
    print("the buyer needs to pay {} shekels".format(dictionary.cart(buyer, shop, BUYER_FILE)))


if __name__ == "__main__":
    main()

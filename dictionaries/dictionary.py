APPEND = "a"
WRITE = "w"
COST = "cost"


def create_dictionary(products, prices):
    return dict(zip(products, prices))


def cart(buyer, shop, file_name):
    buy_sum = 0
    for product in buyer:
        buy_sum += buyer[product] * float(shop[product])
    with open(file_name, APPEND) as file:
        file.write("Total: {}".format(buy_sum))
    return buy_sum


def recieve(buyer, file_path):
    with open(file_path, WRITE) as file:
        for product in buyer:
            prod_format = "product: {}, amount: {}\n".format(product, buyer[product])
            file.write(prod_format)
            print(prod_format)


def create_file(dictionary, file_name, dic_relation, situation):
    with open(file_name, situation) as file:
        for product in dictionary:
            file.write("product: {}, {}: {}\n".format(product, dic_relation, dictionary[product]))


def extract_product_cost(line):
    l = [i for i in range(len(line)) if line[i] == ":"]
    prod = line[l[0] + 2:line.index(",")]
    cost = line[l[1] + 2:-1]
    return prod, cost


def change_price(product, cost, file_name):
    shop = from_file_to_dict(file_name)
    shop[product] = cost
    create_file(shop, file_name, COST, WRITE)
    print("the cost changed successfully\n")


def from_file_to_dict(file_name):
    shop = []
    with open(file_name, "r") as file:
        for line in file:
            shop += [extract_product_cost(line)]
    shop = dict(shop)
    return shop


def check_product(file_name, product):
    shop = from_file_to_dict(file_name)
    if product not in shop:
        return True
    return False


def minus_prod(l, term):
    return [i for i in l if i != term]


def minus_num(l, place):
    return l[0:place] + l[place + 1:]


def delete_product(file_name, product, prod_list, price_list):
    shop = from_file_to_dict(file_name)
    if product not in shop and product not in prod_list:
        print("the product didn't exist\n")
        return prod_list, price_list
    elif product in shop:
        shop.pop(product)
        create_file(shop, file_name, COST, WRITE)
    print("the product {} successfully removed\n".format(product))
    if not prod_list:
        return [], []
    elif product not in prod_list:
        return prod_list, price_list
    num_list = minus_num(price_list, prod_list.index(product))
    return minus_prod(prod_list, product), num_list


def print_product(shop_file):
    shop = ""
    with open(shop_file, "r") as file:
        for line in file:
            shop += line
    return shop

    main()

import pickle
import json


def change_price(product, value):
    product['price'] += value


def change_price_by_percent(product, percent):
    product['price'] *= 1 + (percent / 100)


methods = {
    'add': lambda p, v: change_price(p, v),
    'sub': lambda p, v: change_price(p, -v),
    'percent+': lambda p, v: change_price_by_percent(p, v),
    'percent-': lambda p, v: change_price_by_percent(p, -v),
}

with open("../fourth_task_products.json", "rb") as file:
    products = pickle.load(file)

products_dict = {}
for p in products:
    products_dict[p['name']] = p

with open("../fourth_task_updates.json", "r", encoding='utf-8') as file:
    queries = json.load(file)

for q in queries:
    method = methods[q['method']]
    product = products_dict[q['name']]
    param = float(q['param'])
    method(product, param)

with open('../outputs/task4.pkl', 'wb') as output_file:
    pickle.dump(products, output_file)

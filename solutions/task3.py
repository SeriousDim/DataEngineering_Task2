import json
import numpy as np
import msgpack

with open('../third_task.json', encoding='utf-8') as json_file:
    goods = json.load(json_file)

prices = dict()
for good in goods:
    if good['name'] not in prices.keys():
        prices[good['name']] = []
    prices[good['name']].append(float(good['price']))

result = dict()

for key in prices.keys():
    product_prices = np.array(prices[key])
    result[key] = {
        "mean": float(product_prices.mean()),
        "max": float(product_prices.max()),
        "min": float(product_prices.min())
    }

print(result)

with open('../outputs/task3.json', 'w', encoding='utf-8') as output_file:
    json.dump(result, output_file, ensure_ascii=False, indent=4)

with open('../outputs/task3.msgpack', 'wb') as output_file:
    packed = msgpack.packb(result)
    output_file.write(packed)

"""
task3.json - 11,1 Кб
task3.msgpack - 5,94 Кб
"""

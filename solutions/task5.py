import json
import pickle
import msgpack
import pandas as pd


categorical_fields = ['postcode', 'currentEnergyRating']
numeral_fields = ['bathrooms', 'bedrooms', 'floorAreaSqM', 'rentEstimate_lowerPrice', 'rentEstimate_currentPrice', 'rentEstimate_upperPrice']
fields = [*categorical_fields, *numeral_fields]


houses = pd.read_csv('../london_houses.csv')

stats = {}

for f in numeral_fields:
    column = houses[f]
    stats[f] = {
        "max": float(column.max()),
        "min": float(column.min()),
        "mean": float(column.mean()),
        "sum": float(column.sum()),
        "std": float(column.std())
    }

for f in categorical_fields:
    column = houses[f]
    counts = column.value_counts()
    keys = counts.keys()
    stats[f] = {}
    for k in keys:
        stats[f][k] = int(counts[k])

with open('../outputs/task5/task5.json', 'w') as output_file:
    json.dump(stats, output_file, ensure_ascii=False, indent=4)

# Сохранение в разных форматах
houses[fields].to_csv('../outputs/task5/london_houses_filtered.csv')
houses[fields].to_json('../outputs/task5/london_houses_filtered.json')

with open('../outputs/task5/london_houses_filtered.pkl', 'wb') as output_file:
    pickle.dump(houses[fields], output_file)

with open('../outputs/task5/london_houses_filtered.msg', 'wb') as output_file:
    with open('../outputs/task5/london_houses_filtered.json') as json_file:
        packed = msgpack.packb(json_file.read())
        output_file.write(packed)

"""
CSV - 13,7 Мб
JSON - 31,8 Мб
MSG - 31,8 Мб
PKL - 16,0 Мб
"""

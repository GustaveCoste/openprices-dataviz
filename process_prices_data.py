import json

import pandas as pd

with open("prices.json") as file:
    prices = json.load(file)

records = []
for entry in prices:
    try:
        record = {
            'price': entry['price'],
            'location_id': str(entry['location_id']),
            'product_id': int(entry['product_id']),
            'date': entry['date'],
            'currency': entry['currency']
        }
        records.append(record)
    except TypeError:
        pass

df = pd.DataFrame(records)

df.to_csv("prices.csv", index=False)
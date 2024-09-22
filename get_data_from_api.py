import json

from requests import request
from tqdm import trange

PRICES_API_URL = "https://prices.openfoodfacts.org/api/v1/prices"

first_req = request(method="GET", url=PRICES_API_URL)

nb_pages = first_req.json()["pages"]
prices = []
# for page in trange(1, 10):
for page in trange(1, nb_pages + 1):
    req = request(method="GET", url=PRICES_API_URL, params={"page": page})
    prices += req.json()["items"]

with open('prices.json', 'w') as outfile:
    json.dump(prices, outfile, indent=2)

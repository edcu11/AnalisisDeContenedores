import json
from pprint import pprint

with open('products.json') as f:
    data = json.load(f)

blocks = data["Blocks"]

#print(data["maps"][1]["id"])  # will return 'blabla'
#print(data["masks"]["id"])    # will return 'valore'
#print(data["om_points"])      # will return 'value'

for block in blocks:
        print(int(block["Length"] ) + 5)

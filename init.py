import json
from pprint import pprint

class Block():
    """docstring for Block."""
    def __init__(self, length, height):
        self.length = length
        self.height = height
        self.IsInitial = False

def ProcessBlocks(rawDataBlocks):
    blocks = []
    for b in rawDataBlocks:
        blocks.append(Block(int(b["Length"]), int(b["Height"])))
    return blocks


with open('products.json') as f:
    data = json.load(f)

blocks = ProcessBlocks(data["Blocks"])


for b in blocks:
        print("Length" , b.length, ":" , b.height)



#print(data["maps"][1]["id"])  # will return 'blabla'
#print(data["masks"]["id"])    # will return 'valore'
#print(data["om_points"])      # will return 'value'

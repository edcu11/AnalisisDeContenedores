import json
from pprint import pprint

class Block():
    """docstring for Block."""
    def __init__(self, length, height, initial):
        self.length = length
        self.height = height
        self.IsInitial = initial

class Contenedor():
    """docstring for Contenedor."""
    def __init__(self, dim):
        self.dimensiones = dim
        self.Space = Matrix = [[0 for x in range(dim)] for y in range(1000)]

class PosicionInidice():
    """docstring for PosicionInidice."""
    def __init__(self, x, y):
        self.x = x
        self.y = y



def ProcessBlocks(rawDataBlocks):
    blocks = []
    for b in rawDataBlocks:
        blocks.append(Block(int(b["Length"]), int(b["Height"]),True))
    return blocks


def PosicionValida(bloque, x, y):
    if contenedor[x][y] == None:
        return True
    return False

def AgregarBloque(bloque, Xinicial, Yinicial,contenedor):
    for x in range(bloque.length - 1):
        for y in range(bloque.height - 1):
            contenedor[Xinicial + x][Yinicial + y] = \
            Block(bloque.length, bloque.height, False)

    contenedor [Xinicial][Yinicial] = Block(bloque.length, bloque.height, True)


'''def HayEspacioDisponible():
    pass'''

def EncontrarPosicionDisponible(bloque):
    for linea in contenedor.Space:
        for indice in linea:
            if HayEspacioDisponible(bloque):
                return PosicionInidice(linea, indice)
    return PosicionInidice(-1, -1)


def IntentarAgregarBloque(bloque):
    posicion = EncontrarPosicionDisponible(bloque)
    if posicion.x == -1 or posicion.y == -1:
        return false
    AgregarBloque(bloque)

def CantHuecos(self):
    cant = 0
    for x in range(contenedor.dimensiones):
        for y in range(1000):
            if(contenedor[x][y] == None):
                cant+=1
    return cant

with open('products.json') as f:
    data = json.load(f)

global contenedor
contenedor = Contenedor(10)
blocks = ProcessBlocks(data["Blocks"])

for b in blocks:
    print("Length" , b.length, ":" , b.height)

AgregarBloque(blocks[0],0,0)





#print(data["maps"][1]["id"])  # will return 'blabla'
#print(data["masks"]["id"])    # will return 'valore'
#print(data["om_points"])      # will return 'value'

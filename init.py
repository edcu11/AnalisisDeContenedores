import json
from pprint import pprint


class Block():
    """docstring for Block."""
    def __init__(self, length, height, initial):
        self.length = length
        self.height = height
        self.IsInitial = initial
        self.IsValid = True

class Contenedor():
    """docstring for Contenedor."""
    def __init__(self, dim,altura):
        self.dimensiones = dim
        self.altura = altura
        self.Space = Matrix = [[None for x in range(altura)] for y in range(dim)]

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

def PosicionValida(x,y):
    if contenedor.Space[x][y] == None:
        return True
    return False

def AgregarBloque(bloque,Xinicial,Yinicial):
    for y in range(Yinicial,Yinicial + bloque.height):
        for x in range(Xinicial,Yinicial + bloque.length):
            contenedor.Space[x][y] = Block(bloque.length, bloque.height, False)
            print('Agregando En:',x,',',y)

    contenedor.Space[Xinicial][Yinicial] = Block(bloque.length, bloque.height, True)
    

def HayEspacioDisponible(bloque,indice,linea):
    for y in range(linea,linea + bloque.height):
        for x in range(indice,indice + bloque.length):
            print(x,y)
            if x > 9:
                return False
            if PosicionValida(x,y) == False:
                return False   
    return True

def EncontrarPosicionDisponible(bloque):
    for y in range(0,contenedor.altura):
        for x in range(0,contenedor.dimensiones):
            if HayEspacioDisponible(bloque,x,y):
                return PosicionInidice(x, y)

    return PosicionInidice(-1, -1)

def IntentarAgregarBloque(bloque):
    posicion = EncontrarPosicionDisponible(bloque)
    if posicion.x == -1 or posicion.y == -1:
        return false
    AgregarBloque(bloque,posicion.x,posicion.y)

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
contenedor = Contenedor(10,1000)
blocks = ProcessBlocks(data["Blocks"])

#AgregarBloque(blocks[0],0,0)
#AgregarBloque(blocks[1],6,0)

IntentarAgregarBloque(blocks[0])
#IntentarAgregarBloque(blocks[1])
IntentarAgregarBloque(blocks[2])
IntentarAgregarBloque(blocks[4])
IntentarAgregarBloque(blocks[5])

#print ('Length:',contenedor.Space[6][0].length,'Height:',contenedor.Space[6][0].height)
#print ('Length:',contenedor.Space[0][0].length,'Height:',contenedor.Space[0][0].height)
 



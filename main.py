import random
import numpy as np
def prob(n:int):
    list = [1]
    for m in range(n-1):
        list.append(0)
    return random.choice(list) == 1


class Tile:
    def __init__(self):
        self.__contents:dict = {"cell":None,"materials":set()}
        
    def addMaterials(self,materials:list):
        self.__contents["materials"].add(*materials)
        
    def clearMaterials(self,materials:list):
         ans  = self.__contents["materials"]
         self.__contents["materials"].clear(*materials)
         return ans
     
class Cell:
    def __init__(self,materials,gene,x,y,energy=100,hp=100):
        self.__materials:list = materials
        self.__gene:str = gene
        self.__x:int = x
        self.__y:int = y
        self.__energy:float = energy
        self.__hp:float = hp
        if hp < 0:
            raise ValueError("hp must be positive")
        if energy < 0:
            raise ValueError("energy must be positive")
        
    def 

class Field:
    def __init__(self,field_n):
        self.__field_n = field_n
        self.__field = np.full((),Tile())
        
    def setRandomCell(self,num):
        
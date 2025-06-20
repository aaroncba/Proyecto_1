from dataclasses import dataclass, asdict
from bson import ObjectId
from typing import Optional

@dataclass
class Laptop:
    id_laptop : int
    marca : str
    modelo : str
    #esto ayudara a que se guarde empleado_id como ObjectId
    empleado_id: Optional[ObjectId] = None
    
    def __init__(self, id_laptop, marca, modelo):
        self.id_laptop = id_laptop
        self.marca = marca
        self.modelo = modelo    
        
    def save(self, coll):
        return str(coll.insert_one(asdict(self)).inserted_id) 


from dataclasses import dataclass, asdict
from bson import ObjectId
from typing import Optional

@dataclass
class Empleado:
    
    id_empleado: int
    nombre: str
    departamento: str
    correo: str
    id_laptop : Optional[ObjectId] = None
    

    def __init__(self, id_empleado, nombre, departamento, correo):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.departamento = departamento
        self.correo = correo


    def save(self, coll):
        return str(coll.insert_one(asdict(self)).inserted_id) 
         

    


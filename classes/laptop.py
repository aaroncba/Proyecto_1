from dataclasses import dataclass, asdict

@dataclass
class Laptop:
    id_laptop : int
    marca : str
    modelo : str
    empleado_id: str = ""

    def __init__(self, id_laptop, marca, modelo):
        self.id_laptop = id_laptop
        self.marca = marca
        self.modelo = modelo
        
    def save(self, coll):
        return str(coll.insert_one(asdict(self)).inserted_id)


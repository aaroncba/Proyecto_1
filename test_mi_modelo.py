import unittest
from bson import ObjectId
from dotenv import load_dotenv
from pymongo import MongoClient
from app import actualizar_documento
import os

from classes.empleado import Empleado
from classes.laptop import Laptop


load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
db = client["empresa"]
empleados = db["empleados"]
laptops = db["laptops"]

class TestRelacionUnoAUno(unittest.TestCase): 

    def test_laptop_asignada_empleado(self): 
        
        #definimos al empleado
        emp = Empleado(2312, "Eduardo PieGrande", "Investigacion", "eduardo@yahoo.com")
        emp_id = emp.save(empleados)
        
        laptop = Laptop(98123, "DELL", "XPS-13")
        laptop.empleado_id = emp_id
        laptop_id = laptop.save(laptops)

        laptop_asignada = laptops.find_one({"_id": ObjectId(laptop_id)})
        self.assertEqual(laptop_asignada["empleado_id"], emp_id)

    def test_empleado_asignado_laptop_correcta(self): 
        emp = Empleado(4589, "María González", "Desarrollo", "maria.gonzalez@example.com")
        emp_id = emp.save(empleados)

        laptop = Laptop(75231, "Apple", "MacBook Pro 16")
        laptop.empleado_id = emp_id
        laptop_id = laptop.save(laptops)
        
        actualizar_documento(laptop_id, emp_id, empleados)
        #necesito saber si el laptop_id en empleado_id es igual al laptop_id
        empleado_actualizado = empleados.find_one({"_id": ObjectId(emp_id)})
        print(str(empleado_actualizado["id_laptop"]))
        print(laptop_id)
        self.assertEqual(str(empleado_actualizado["id_laptop"]), laptop_id)


if __name__ == "__main__": 
    unittest.main()

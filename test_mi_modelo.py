import unittest
from bson import ObjectId
from dotenv import load_dotenv
from pymongo import MongoClient
from app import actualizar_documento
import os

from classes.empleado import Empleado
from classes.laptop import Laptop

#iniciando la conexion con MongoDB
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
        #definimos una laptop
        laptop = Laptop(98123, "DELL", "XPS-13")
        #tomamos el _id del empleado creado antes 
        #y lo guardamos en empleado_id dentro de laptop
        laptop.empleado_id = ObjectId(emp_id)
        #Se guarda todo en la db
        laptop_id = laptop.save(laptops)

        #agregando laptop_id a emp_id
        actualizar_documento(laptop_id, emp,emp_id, empleados)
        
        #Buscamos el id de la laptop dentro de la db
        #con laptop_id buscamos el empleado_id para compararlo con emp_id que tenemos
        laptop_asignada = laptops.find_one({"_id": ObjectId(laptop_id)})
        self.assertEqual(laptop_asignada["empleado_id"], ObjectId(emp_id))

        


    def test_empleado_asignado_laptop_correcta(self): 
        #creamos un empleado y lo guardamos en la db 
        emp = Empleado(4589, "María González", "Desarrollo", "maria.gonzalez@example.com")
        emp_id = emp.save(empleados)

        #creamos una laptop, le agregamos el emp_id y lo guardamos en la db 
        laptop = Laptop(75231, "Apple", "MacBook Pro 16")
        laptop.empleado_id = ObjectId(emp_id)
        laptop_id = laptop.save(laptops)
        
        #actualizamos el laptop_id dentro del empleado
        actualizar_documento(laptop_id, emp, emp_id, empleados)
        #Obtenemos el documento de emp_id
        #dentro de este documento buscamos id_laptop para compararlo con el laptop_id
        empleado_actualizado = empleados.find_one({"_id": ObjectId(emp_id)})
        self.assertEqual(str(empleado_actualizado["id_laptop"]), laptop_id)


if __name__ == "__main__": 
    unittest.main()

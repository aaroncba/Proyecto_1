from classes.empleado import Empleado
from classes.laptop import Laptop
from pymongo import MongoClient
from dotenv import load_dotenv
from bson.objectid import ObjectId
import os

def main():
    # Connect to MongoDB
    load_dotenv()
    client = MongoClient(os.getenv("MONGO_URI"))
    db = client["empresa"]
    empleados = db["empleados"]
    laptops = db["laptops"]

    # Create and save an employee
    emp = Empleado(12, "Carlos", "Ventas", "carlos@gmail.com")
    emp_id = emp.save(empleados)

    print(f"Empleado guardado con ID: {emp_id}")

    emp = Empleado(134, "Aaron", "Marketing", "aaron@gmail.com")
    emp_id = emp.save(empleados)

    print(f"Empleado guardado con ID: {emp_id}")

    
    laps = Laptop(1234, "Lenovo", "L204") 
    #esta laptop se la voy a asignar a Aaron
    laps.empleado_id = emp_id 
    laptop_id = laps.save(laptops)

    print(f"Laptop guardada con ID: {laptop_id}")

    actualizar_documento(laptop_id, emp_id, empleados)

#id_documento = laptop -> id_relacion = empleado

def actualizar_documento(laptop_id, empleado_id, empleados_collection): 
    filtro = {"_id": ObjectId(empleado_id)}  
    nuevos_valores = {"$set": {"id_laptop": ObjectId(laptop_id)}}  
    resultado = empleados_collection.update_one(filtro, nuevos_valores)
    
    if resultado.matched_count > 0:
        print("Empleado actualizado correctamente con el ID de laptop.")
    else:
        print("No se encontró ningún empleado con ese ID.")
    
    return resultado


if __name__ == "__main__":
    main()

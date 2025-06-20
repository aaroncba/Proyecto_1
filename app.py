from classes.empleado import Empleado
from classes.laptop import Laptop
from pymongo import MongoClient
from dotenv import load_dotenv
from bson.objectid import ObjectId
import os

def main():
    # Inicio de conexion con MongoDB
    load_dotenv()
    client = MongoClient(os.getenv("MONGO_URI"))
    db = client["empresa"]
    empleados = db["empleados"]
    laptops = db["laptops"]

    # Creamos y guardamos el empleado
    emp = Empleado(12, "Carlos", "Ventas", "carlos@gmail.com")
    emp_id = emp.save(empleados)
    #confirmacion en terminal que se guardo el empleado 
    print(f"Empleado guardado con ID: {emp_id}")
    #creamos un segundo empleado
    emp = Empleado(134, "Aaron", "Marketing", "aaron@gmail.com")
    emp_id = emp.save(empleados)
    #confirmacion del segundo empleado 
    print(f"Empleado guardado con ID: {emp_id}")

    #creamos una laptop
    laps = Laptop(1234, "Lenovo", "L204") 
    #esta laptop se la voy a asignar a Aaron
    laps.empleado_id = ObjectId(emp_id) 
    laptop_id = laps.save(laptops)

    #confirmacion que se guardo la laptop
    print(f"Laptop guardada con ID: {laptop_id}")
    #actualizamos el documento de empleado para agregar el laptop_id
    actualizar_documento(laptop_id, emp,emp_id, empleados)
    
    
#parametro para funcion: 
#laptop_id -> _id
#instancia de empleado: para poder agregar el id de la laptop a la instancia de empleado, en caso de ser necesario.
def actualizar_documento(laptop_id, empleado, empleado_id, empleados_collection): 
    
    #definimos el filtro para encontrar el documento de empleado_id
    filtro = {"_id": ObjectId(empleado_id)}  
    
    nuevos_valores = {"$set": {"id_laptop": ObjectId(laptop_id)}}  
    resultado = empleados_collection.update_one(filtro, nuevos_valores)
    
    if resultado.matched_count > 0:
        empleado.id_laptop = laptop_id
        print("Empleado actualizado correctamente con el ID de laptop.")
    else:
        print("No se encontró ningún empleado con ese ID.")
    
    return resultado


if __name__ == "__main__":
    main()

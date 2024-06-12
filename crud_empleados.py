import os
import json
os.system("cls ")

def cargar_json(url_arhivo):
    with open(url_arhivo, 'r') as archivo:
        return json.load(archivo)
    
empleados = cargar_json("empleados.json")

print (empleados)
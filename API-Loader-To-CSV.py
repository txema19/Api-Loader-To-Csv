import requests
import csv

#Programa para cargar una API con todas sus tablas en un fichero CSV
filename = 'resultados.csv'
urlAPI="https://swapi.dev/api/" #En este caso la url será de una API de Star Wars

def definirTablas():
    respuesta = requests.get(urlAPI)
    if respuesta.status_code==200:
        datos = respuesta.json()
        return list(datos.keys())
    else:
        print(f"ERROR DE COMUNICACIÓN {respuesta.status_code}")
    

#Metodo para cargar las distintas tablas de la API en formato JSON
def cargarJSON(tabla):
    url=urlAPI+tabla
    respuesta = requests.get(url)
    
    if respuesta.status_code==200:
        datos = respuesta.json()
        return datos["results"]
    else:
        print(f"ERROR DE COMUNICACIÓN {respuesta.status_code}")

#Metodo para convertir el JSON en CSV
def cargarCSV(tabla):
    json = cargarJSON(tabla)
    fields = list(json[0].keys())
    
    with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(json)
        writer.writerow({field: '' for field in fields})
    print("EXITO")

#Metodo principal
def main():
    open(filename, 'w').close()
    tablas=definirTablas()
    for tabla in tablas:
        print("Cargando tabla: "+tabla+"...",end = " ")
        cargarCSV(tabla)
        
    print("FIN DEL PROGRAMA")
    
main()

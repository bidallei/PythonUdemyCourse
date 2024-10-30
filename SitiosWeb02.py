import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Lista de terapias alternativas
terapias = [
    "reiki",
   
]

def buscar_sitios(terapia):
    url = f"https://www.google.com/search?q={terapia}+site:.mx"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Error al acceder a Google: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extraer los enlaces
    enlaces = []
    for item in soup.find_all('a'):
        link = item.get('href')
        if link and "url?q=" in link:
            enlace = link.split("url?q=")[1].split("&")[0]
            enlaces.append(enlace)
    
    return enlaces

def guardar_en_xlsx(data):
    # Crear un DataFrame de pandas
    df = pd.DataFrame(columns=["Terapia", "Enlace"])
    
    for terapia, enlaces in data.items():
        for enlace in enlaces:
            df = df.append({"Terapia": terapia, "Enlace": enlace}, ignore_index=True)
    
    # Guardar el DataFrame en un archivo Excel
    df.to_excel("terapias.xlsx", index=False)

def main():
    resultados = {}
    
    for terapia in terapias:
        print(f"Buscando sitios para: {terapia}")
        sitios = buscar_sitios(terapia)
        resultados[terapia] = sitios
        
        # Esperar un tiempo para evitar bloqueos
        time.sleep(2)  # Esperar 2 segundos entre las búsquedas

    guardar_en_xlsx(resultados)
    print("Resultados guardados en terapias.xlsx")

if __name__ == "__main__":
    main()
 
 
    # "masajes",
    # "acupuntura",
    # "aromaterapia",
    # "meditación guiada",
    # "terapia de cristales",
    # "terapia holística",
    # "lectura de tarot",
    # "limpieza del aura",
    # "sanación con sonido",
    # "shiatsu",
    # "reflexología",
    # "regresiones a vidas pasadas",
    # "chamanismo",
    # "imanes"


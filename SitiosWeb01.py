import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Lista de terapias alternativas
terapias = [
    "acupuntura",
]

def buscar_sitios(terapia):
    url = f"https://www.bing.com/search?q={terapia}+site:.mx"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Error al acceder a Bing: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extraer los enlaces de Bing
    enlaces = []
    for item in soup.find_all('a'):
        link = item.get('href')
        if link and "http" in link:
            enlaces.append(link)
    
    return enlaces

def guardar_en_xlsx(data):
    # Crear un DataFrame vacío
    df = pd.DataFrame(columns=["Terapia", "Enlace"])
    
    for terapia, enlaces in data.items():
        temp_df = pd.DataFrame({"Terapia": [terapia] * len(enlaces), "Enlace": enlaces})
        df = pd.concat([df, temp_df], ignore_index=True)
    
    # Guardar el DataFrame en un archivo Excel
    df.to_excel("terapias03.xlsx", index=False)

def main():
    resultados = {}
    
    for terapia in terapias:
        print(f"Buscando sitios para: {terapia}")
        sitios = buscar_sitios(terapia)
        resultados[terapia] = sitios
        
        # Esperar un tiempo para evitar bloqueos
        time.sleep(10)  # Esperar 10 segundos entre las búsquedas

    guardar_en_xlsx(resultados)
    print("Resultados guardados en terapias.xlsx")

if __name__ == "__main__":
    main()

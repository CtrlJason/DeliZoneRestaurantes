from django.core.cache import cache
import requests

def obtener_paises():
    url = "https://restcountries.com/v3.1/all"
    print("Estoy aqui")
    try:
        respose = requests.get(url)
        respose.raise_for_status()
        data = respose.json()
        paises = sorted([(pais['name']['common'], pais['name']['common']) for pais in data])
        print(paises)
        return paises
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener los países: {e}")
        return []
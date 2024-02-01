import requests

def obtener_informacion_meteorologica(ciudad, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    parametros = {"q": ciudad, "appid": api_key, "units": "metric"}  

    try:
        respuesta = requests.get(base_url, params=parametros)
        datos = respuesta.json()

        if datos["cod"] == "404":
            return f"No se encontraron datos para {ciudad}."

        temperatura = datos["main"]["temp"]
        condiciones = datos["weather"][0]["description"]
        pronostico = f"El tiempo estará {condiciones} con una temperatura de {temperatura} grados Celsius."

        informacion = f"Información meteorológica para {ciudad}:\n{pronostico}"
        return informacion

    except Exception as e:
        return f"Error al obtener datos meteorológicos: {str(e)}"


ciudad_ejemplo = "Ciudad Ejemplo"
api_key_ejemplo = "tu_clave_api"  # Reemplaza con tu clave API de OpenWeatherMap
informacion_ejemplo = obtener_informacion_meteorologica(ciudad_ejemplo, api_key_ejemplo)
print(informacion_ejemplo)

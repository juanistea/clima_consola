import requests

# codigos de clima de Open-Meteo mas comunes
DESCRIPCIONES = {
    0: "Despejado",
    1: "Mayormente despejado",
    2: "Parcialmente nublado",
    3: "Nublado",
    45: "Niebla",
    51: "Llovizna leve",
    53: "Llovizna",
    55: "Llovizna fuerte",
    61: "Lluvia leve",
    63: "Lluvia",
    65: "Lluvia fuerte",
    80: "Chaparrones leves",
    81: "Chaparrones",
    82: "Chaparrones fuertes",
    95: "Tormenta",
}


def buscar_ciudad(nombre: str) -> dict | None:
    """Busca una ciudad por nombre y devuelve sus datos.

    parametro nombre: Nombre de la ciudad a buscar.

    devuelve: Diccionario con nombre, país, latitud y longitud,
    o None si no se encontró la ciudad.
    """
    url = "https://geocoding-api.open-meteo.com/v1/search"
    parametros = {"name": nombre, "count": 1, "language": "es"}
    respuesta = requests.get(url, params=parametros)

    # caso de no encontrar
    if respuesta.status_code != 200:
        return None

    datos = respuesta.json()

    # caso de no encontrar la ciudad
    if "results" not in datos:
        return None

    ciudad = datos["results"][0]

    return {
        "nombre": ciudad["name"],
        "pais": ciudad["country"],
        "latitud": ciudad["latitude"],
        "longitud": ciudad["longitude"],
    }


def obtener_clima(latitud: float, longitud: float) -> dict | None:
    """Pide el clima actual y el pronóstico de los próximos días.

    parametro latitud: Latitud de la ciudad.
    parametro longitud: Longitud de la ciudad.

    devuelve: Diccionario con el clima "actual" y el "diario",
    o None si la API respondió con error.
    """
    url = "https://api.open-meteo.com/v1/forecast"
    parametros = {
        "latitude": latitud,
        "longitude": longitud,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m,"
                   "weather_code",
        "daily": "temperature_2m_max,temperature_2m_min,weather_code",
        "timezone": "auto",
        "forecast_days": 5,
    }
    respuesta = requests.get(url, params=parametros)

    # caso de error
    if respuesta.status_code != 200:
        return None

    datos = respuesta.json()

    return {
        "actual": datos["current"],
        "diario": datos["daily"]
    }


def describir_codigo(codigo: int) -> str:
    """Traduce el código de clima de la API a un texto en castellano.

    parametro codigo: Código numérico de clima.

    devuelve: Descripción del clima, o "Sin datos" si el código
    no está en la lista.
    """
    if codigo in DESCRIPCIONES:
        return DESCRIPCIONES[codigo]
    return "Sin datos"

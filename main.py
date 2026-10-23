import requests

from clima import buscar_ciudad, obtener_clima
from vista import consola, mostrar_bienvenida, mostrar_error
from vista import mostrar_clima_actual, mostrar_pronostico


def consultar(nombre_ciudad: str) -> None:
    """Busca la ciudad, pide el clima y lo muestra.

    parametro nombre_ciudad: Nombre de la ciudad que escribió el usuario.
    """
    try:
        ciudad = buscar_ciudad(nombre_ciudad)

        if ciudad is None:
            mostrar_error(f"No encontré la ciudad '{nombre_ciudad}'.")
            return

        datos = obtener_clima(ciudad["latitud"], ciudad["longitud"])

        if datos is None:
            mostrar_error("No se pudo obtener el clima.")
            return

    except requests.RequestException:
        mostrar_error("No se pudo conectar. Revisá tu conexión a internet.")
        return

    mostrar_clima_actual(ciudad, datos["actual"])
    mostrar_pronostico(datos["diario"])


def main() -> None:
    """Pide ciudades hasta que el usuario escriba 'salir'."""

    mostrar_bienvenida()

    while True:
        nombre = consola.input("\n[bold]Ciudad:[/bold] ").strip()

        if nombre.lower() == "salir":
            break
        if nombre == "":
            mostrar_error("Tenés que escribir el nombre de una ciudad.")
            continue

        consultar(nombre)

    consola.print("¡Chau!")


if __name__ == "__main__":
    main()

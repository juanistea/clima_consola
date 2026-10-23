from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from clima import describir_codigo

consola = Console()


def mostrar_bienvenida() -> None:
    """Muestra el título del programa."""

    texto = "[bold cyan]Clima por consola[/bold cyan]\n"
    texto += "Escribí una ciudad o 'salir' para terminar."
    consola.print(Panel(texto, expand=False))


def mostrar_clima_actual(ciudad: dict, actual: dict) -> None:
    """Muestra el clima de este momento en un panel.

    parametro ciudad: Datos de la ciudad (nombre y país).
    parametro actual: Datos del clima actual que devuelve la API.
    """

    texto = (
        f"Temperatura: [bold]{actual['temperature_2m']} °C[/bold]\n"
        f"Humedad: {actual['relative_humidity_2m']} %\n"
        f"Viento: {actual['wind_speed_10m']} km/h\n"
        f"Estado: {describir_codigo(actual['weather_code'])}"
    )

    titulo = f"{ciudad['nombre']}, {ciudad['pais']}"
    panel = Panel(texto, title=titulo, border_style="green", expand=False)
    consola.print(panel)


def mostrar_pronostico(diario: dict) -> None:
    """Muestra una tabla con el pronóstico de los próximos días.

    parametro diario: Datos diarios que devuelve la API
    (fechas, mínimas y máximas).
    """
    tabla = Table(title="Pronóstico")
    tabla.add_column("Fecha", style="cyan")
    tabla.add_column("Mínima", justify="right", style="blue")
    tabla.add_column("Máxima", justify="right", style="red")
    tabla.add_column("Estado")

    for i in range(len(diario["time"])):
        fecha = diario["time"][i]
        minima = f"{diario['temperature_2m_min'][i]} °C"
        maxima = f"{diario['temperature_2m_max'][i]} °C"
        estado = describir_codigo(diario["weather_code"][i])
        tabla.add_row(fecha, minima, maxima, estado)

    consola.print(tabla)


def mostrar_error(mensaje: str) -> None:
    """Muestra un mensaje de error en rojo.

    parametro mensaje: Texto del error.
    """
    consola.print(f"[bold red]Error:[/bold red] {mensaje}")

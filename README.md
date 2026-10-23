# Clima por consola

Trabajo de la Unidad 11 de Programación 1 (ISTEA), **Opción B: mini proyecto propio**.

Es un programa de consola donde escribís el nombre de una ciudad y te muestra el clima actual (temperatura, humedad, viento) y el pronóstico de los próximos 5 días en una tabla con colores. Los datos salen de la API gratuita de [Open-Meteo](https://open-meteo.com/), que no pide registrarse ni clave.

## Librerías que usa

| Librería | Para qué la usé |
|----------|-----------------|
| `requests` | Hacer los pedidos HTTP a la API de Open-Meteo |
| `rich` | Mostrar el resultado con paneles, tablas y colores |

## Estructura

```text
clima_consola/
├── .gitignore
├── README.md
├── requirements.txt
├── main.py      ← punto de entrada, pide la ciudad y maneja los errores
├── clima.py     ← funciones que consultan la API
└── vista.py     ← funciones que muestran todo en la consola
```

## Instalación

Hace falta tener Python 3 instalado.

```bash
git clone <url-del-repo>
cd clima_consola
python -m venv .venv
```

Activar el entorno virtual:

```bash
.venv\Scripts\activate         # Windows
source .venv/bin/activate      # Linux / Mac
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Cómo se ejecuta

```bash
python main.py
```

Escribís una ciudad (por ejemplo `Buenos Aires` o `Córdoba`) y para terminar escribís `salir`.

## Manejo de errores

- Si dejás la ciudad vacía, te avisa y te la vuelve a pedir.
- Si la ciudad no existe, muestra un mensaje y sigue funcionando.
- Si no hay internet, avisa en vez de cortarse.

## Integrantes

- Juan Ignacio Lotito
- Julio Sejas
- Tomas Peña

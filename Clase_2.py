"""
Clase_2: Introducción a Funciones, Módulos y Manejo de Archivos

Esta clase cubre los conceptos fundamentales de:
- Creación y uso de funciones
- Organización de código en módulos (importaciones)
- Validación de entrada del usuario
- Manejo de archivos de texto
- Estructuras de datos (diccionarios)
- Flujo de control y bucles

Proyecto: Juego de Adivinanza de Números con Historial
Un juego interactivo que mantiene el historial de partidas en un archivo de texto.

Módulos utilizados:
- validaciones.py: Funciones para validar y obtener datos del usuario
- juego_numero_secreto.py: Funciones para el juego y gestión del historial
- main.py: Punto de entrada y flujo principal
"""

from validaciones import consigue_y_valida, consigue_y_valida_edad # type: ignore
from juego_numero_secreto import (
    generar_nombre_archivo_historial,
    crear_archivo_historial,
    jugar_adivinanza_numero_secreto,
    pregunta_si_no
) # type: ignore


def ejecutar_juego_adivinanza() -> None: # type: ignore
    """
    Ejecuta el juego de adivinanza de números con historial de partidas.
    
    Flujo:
    1. Solicita y valida nombre del usuario (solo letras y espacios)
    2. Solicita y valida edad del usuario (entre 15 y 100 años)
    3. Genera nombre del archivo de historial basado en nombre y edad
    4. Crea o abre el archivo de historial con estadísticas
    5. Inicia bucle de juego:
       - Genera número aleatorio entre 1 y 100
       - Usuario realiza adivinanzas hasta acertar
       - Registra intentos en el historial
       - Actualiza estadísticas globales
       - Pregunta si desea jugar otra partida
    6. Al salir, muestra mensaje de despedida
    
    Características:
    - Validación completa de entradas
    - Historial persistente en archivo de texto
    - Estadísticas por partida y globales
    - Múltiples partidas en una sesión
    - Interfaz amigable con separadores visuales
    """
    nombre = consigue_y_valida("nombre de pila")
    print(f"Hola {nombre}")

    edad = consigue_y_valida_edad(15, 100)
    print(f"Su edad es: {edad}")
    
    archivo_historial = generar_nombre_archivo_historial(nombre, edad)
    crear_archivo_historial(archivo_historial, nombre, edad)

    # Bucle principal del juego
    while True:
        jugar_adivinanza_numero_secreto(nombre, edad, archivo_historial)
        
        if not pregunta_si_no("¿Quieres jugar otra partida?"):
            print(f"\n¡Gracias {nombre}! Hasta pronto.")
            break


if __name__ == '__main__':
    ejecutar_juego_adivinanza()

"""
Módulo para el juego de adivinanza de números con historial de partidas.

Contiene todas las funciones necesarias para jugar, gestionar
el historial y administrar las estadísticas de las partidas.
"""

import random
import os
import datetime
from validaciones import obtener_numero_desde_teclado # type: ignore


def generar_nombre_archivo_historial(nombre: str, edad: int) -> str:
    """Genera el nombre del archivo de historial de juegos basado en nombre y edad.
    
    Args:
        nombre: Nombre del usuario
        edad: Edad del usuario
        
    Returns:
        Nombre del archivo de historial
    """
    nombre_limpio = nombre.lower().replace(" ", "_")
    return f"{nombre_limpio}_{edad}_historial_juegos.txt"


def crear_archivo_historial(nombre_archivo: str, nombre_usuario: str, edad: int) -> None:
    """Crea o abre el archivo de historial de juegos.
    Si el archivo no existe, lo crea con contenido inicial.
    Si ya existe, lo abre para agregar nuevas partidas.
    
    Args:
        nombre_archivo: Nombre del archivo a crear/abrir
        nombre_usuario: Nombre del usuario
        edad: Edad del usuario
    """
    if os.path.exists(nombre_archivo):
        print(f"✓ Archivo '{nombre_archivo}' encontrado. Continuando con el historial actual...")
    else:
        contenido = f"""{'='*60}
HISTORIAL DE JUEGOS - ADIVINANZAS
{'='*60}

Jugador: {nombre_usuario}
Edad: {edad} años
Fecha de creación: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}

{'='*60}
ESTADÍSTICAS GENERALES
{'='*60}
Partidas jugadas: 0
Intentos totales: 0

{'='*60}
REGISTRO DETALLADO DE PARTIDAS
{'='*60}
"""
        with open(nombre_archivo, 'w', encoding='utf-8') as f:
            f.write(contenido)
        print(f"✓ Archivo '{nombre_archivo}' creado exitosamente")


def actualizar_estadisticas(nombre_archivo: str, intentos_partida: int) -> None:
    """Actualiza las estadísticas del archivo: incrementa partidas en 1 y suma los intentos.
    
    Args:
        nombre_archivo: Nombre del archivo de historial
        intentos_partida: Número de intentos de la partida completada
    """
    with open(nombre_archivo, 'r', encoding='utf-8') as f:
        lineas = f.readlines()
    
    # Buscar y actualizar las líneas de estadísticas
    for i, linea in enumerate(lineas):
        if linea.startswith("Partidas jugadas:"):
            partidas_actuales = int(linea.split(": ")[1].strip())
            lineas[i] = f"Partidas jugadas: {partidas_actuales + 1}\n"
        elif linea.startswith("Intentos totales:"):
            intentos_actuales = int(linea.split(": ")[1].strip())
            lineas[i] = f"Intentos totales: {intentos_actuales + intentos_partida}\n"
    
    with open(nombre_archivo, 'w', encoding='utf-8') as f:
        f.writelines(lineas)


def mostrar_estadisticas(nombre_archivo: str) -> None:
    """Lee y muestra las estadísticas actualizadas del archivo de historial.
    
    Args:
        nombre_archivo: Nombre del archivo de historial
    """
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as f:
            lineas = f.readlines()
        
        print("\n" + "="*60)
        print("ESTADÍSTICAS ACTUALIZADAS")
        print("="*60)
        
        for linea in lineas:
            if linea.startswith("Partidas jugadas:") or linea.startswith("Intentos totales:"):
                print(linea.strip())
        
        print("="*60 + "\n")
        
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{nombre_archivo}'")


def obtener_numero_partida(nombre_archivo: str) -> int:
    """Obtiene el número de partida siguiente basado en las partidas jugadas.
    
    Args:
        nombre_archivo: Nombre del archivo de historial
        
    Returns:
        Número de la próxima partida
    """
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as f:
            lineas = f.readlines()
        
        for linea in lineas:
            if linea.startswith("Partidas jugadas:"):
                partidas_actuales = int(linea.split(": ")[1].strip())
                return partidas_actuales + 1
        
        return 1
    except FileNotFoundError:
        return 1


def obtener_intentos_globales(nombre_archivo: str) -> int:
    """Obtiene el número de intentos globales del archivo de historial.
    
    Args:
        nombre_archivo: Nombre del archivo de historial
        
    Returns:
        Número de intentos totales acumulados
    """
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as f:
            lineas = f.readlines()
        
        for linea in lineas:
            if linea.startswith("Intentos totales:"):
                return int(linea.split(": ")[1].strip())
        
        return 0
    except FileNotFoundError:
        return 0


def crear_partida_actual(numero_secreto: int) -> dict: # type: ignore
    """Crea la estructura de datos para la partida actual.
    
    Args:
        numero_secreto: El número a adivinar
        
    Returns:
        Diccionario con la información de la partida actual
    """
    return {
        "fecha_hora": datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
        "intentos_partida": 0,
        "numero_secreto": numero_secreto
    }


def guardar_partida_completada(nombre_archivo: str, partida: dict, numero_partida: int) -> None: # type: ignore
    """Guarda la información de la partida completada en el archivo de historial.
    
    Args:
        nombre_archivo: Nombre del archivo de historial
        partida: Diccionario con la información de la partida
        numero_partida: Número secuencial de la partida
    """
    with open(nombre_archivo, 'a', encoding='utf-8') as f:
        f.write(f"\n[Partida #{numero_partida}]\n")
        f.write(f"  Fecha y Hora: {partida['fecha_hora']}\n")
        f.write(f"  Intentos: {partida['intentos_partida']}\n")
        f.write(f"  Número Secreto: {partida['numero_secreto']}\n")
        f.write("-" * 60 + "\n")


def jugar_adivinanza_numero_secreto(nombre: str, edad: int, archivo_historial: str) -> None: # type: ignore
    """Realiza una partida completa del juego de adivinanza de números.
    
    Args:
        nombre: Nombre del usuario
        edad: Edad del usuario
        archivo_historial: Ruta del archivo de historial de juegos
    """
    # Obtener intentos globales actuales
    intentos_globales = obtener_intentos_globales(archivo_historial)
    
    # Obtener número de la próxima partida
    numero_partida = obtener_numero_partida(archivo_historial)
    
    # Generar número secreto y crear estructura de la partida actual
    numero_secreto = random.randint(1, 100)
    partida_actual = crear_partida_actual(numero_secreto)

    print(f"\n{'='*60}")
    print(f"PARTIDA #{numero_partida}")
    print(f"{'='*60}")
    print("Pienso en un número entre 1 y 100...")

    while True:
        adivinanza = obtener_numero_desde_teclado("Adivina el número", 1, 100)
        partida_actual["intentos_partida"] += 1

        if adivinanza < numero_secreto:
            print("Demasiado bajo. Intenta de nuevo.")
        elif adivinanza > numero_secreto:
            print("Demasiado alto. Intenta de nuevo.")
        else:
            print(f"\n¡Correcto! Adivinaste el número en {partida_actual['intentos_partida']} intentos.")
            print(f"Intentos globales acumulados: {intentos_globales + partida_actual['intentos_partida']}")
            
            # Actualizar estadísticas y guardar partida
            actualizar_estadisticas(archivo_historial, partida_actual['intentos_partida'])
            guardar_partida_completada(archivo_historial, partida_actual, numero_partida)
            mostrar_estadisticas(archivo_historial)
            break


def pregunta_si_no(mensaje: str) -> bool: # type: ignore
    """Realiza una pregunta de sí/no al usuario.
    
    Args:
        mensaje: Mensaje de la pregunta
        
    Returns:
        True si responde 's' o 'si', False si responde 'n' o 'no'
    """
    while True:
        respuesta = input(f"{mensaje} (s/n): ").lower().strip()
        if respuesta in ['s', 'si']:
            return True
        elif respuesta in ['n', 'no']:
            return False
        else:
            print("Por favor, responde con 's' (sí) o 'n' (no).")

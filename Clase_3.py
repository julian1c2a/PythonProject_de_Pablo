"""
Comenzamos con variables y tipos de datos
y llamadas a funciones

Tipos de Variables Atómicas:
- int: Números enteros (ej: 1, -5, 0)
- float: Números decimales (ej: 3.14, -0.001)
- str: Cadenas de texto (ej: "Hola", 'Mundo')
- bool: Valores booleanos (True, False)

Tipos de Variables Compuestas:
- list: Listas ordenadas y modificables (ej: [1, 2, 3, 1], ["a", "b", "c", "a"])
- tuple: Tuplas ordenadas e inmutables (ej: (1, 2, 3), ("x", "y", "z"))
- dict: Diccionarios de pares clave-valor (ej: {"nombre": "Alice", "edad": 30})
- set: Conjuntos de elementos únicos (ej: {1, 2, 3, 4, 5, 1}) // El 1 repetido se elimina

Estructuras de control:
   - Llamadas a funciones
   - Ciclos for y while
   - Condicionales if-else
   - Estructura match-case

Definición de funciones
"""

def suma_desde_1_hasta_n(n: int) -> int:
    """Calcula la suma de los números enteros desde 1 hasta n.
    
    Args:
        n: Número entero hasta el cual se sumará (inclusive)
        
    Returns:
        La suma total desde 1 hasta n
    """
    if n < 1:
        return 0
    total = 0
    i = 1
    while i < n+1:
        total = total + i
        i = i + 1
    return total

    
if __name__ == '__main__':
    # limite : int = int(input("Ingrese un número entero positivo: "))
    # suma : int = suma_desde_1_hasta_n(limite)
    # mensaje : str = f'La suma desde 1 hasta {limite} es: {suma}'
    # print(mensaje)

    # dia_de_semana : str = input("Ingrese un día de la semana: ")
    # dia_semana_num : int = 0
    # match dia_de_semana.lower():
    #     case "lunes":
    #         dia_semana_num = 1
    #     case "martes":
    #         dia_semana_num = 2
    #     case "miércoles" | "miercoles":
    #         dia_semana_num = 3
    #     case "jueves":
    #         dia_semana_num = 4
    #     case "viernes":
    #         dia_semana_num = 5 
    #     case "sábado" | "sabado":
    #         dia_semana_num = 6
    #     case "domingo":
    #         dia_semana_num = 7

    # if dia_semana_num == 0:
    #     print("El día de la semana ingresado no es válido.")
    # else:
    #     print(f"El día de la semana ingresado es: {dia_de_semana}, {dia_semana_num} de la semana.")

    # Número_de_la_semana : int = 1
    # Número_decimal : float = 3.14
    # Día_de_la_semana : str = "lunes"
    # Si_o_no : bool = True

    primos : list[int] = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    nombres_de_numeros : list[str] = ["cero", "uno", "dos", "tres"]
    caracteristicas_de_personas : tuple[str, int] = ("nombre", 1966)
    asocicación_de_datos_de_personas : dict[str, int] = {"Julián": 1966, "Pablo": 2003}
    conjunto_de_números_primos : set[int] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29}

    print(f'{primos}, lista primos')
    primos.append(31)
    print(f'{primos}, lista primos')
    numeros = primos.copy()
    print(f'{numeros}, lista números')
    numeros.append(37)
    print(f'{numeros}, lista números')
    print(f'{primos}, lista primos')
    primos.extend(numeros)
    print(f'{primos}, lista primos extendida con números')
    
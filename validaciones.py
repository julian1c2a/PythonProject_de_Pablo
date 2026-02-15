"""
Módulo de validaciones para entrada de datos del usuario.

Contiene funciones para validar y obtener nombres y edades
con restricciones específicas.
"""


def is_valid_name(s: str) -> bool:
    """Valida un nombre permitiendo espacios iniciales y finales,
    exige al menos una letra y sólo admite letras y espacios.
    Además asegura que el primer y último carácter no-blanco sean letras,
    de modo que no haya signos o dígitos después de la parte alfabética.
    """
    if s is None: # type: ignore
        return False
    # Debe contener al menos una letra
    if not any(ch.isalpha() for ch in s):
        return False
    # Sólo letras o espacios permitidos
    if not all(ch.isalpha() or ch.isspace() for ch in s):
        return False
    # Primer carácter no-espacio debe ser letra y además debe ser mayúscula
    first_alpha_index = None
    for idx, ch in enumerate(s):
        if not ch.isspace():
            if not ch.isalpha():
                return False
            first_alpha_index = idx
            if not ch.isupper():
                return False
            break
    # Último carácter no-espacio debe ser letra
    for ch in reversed(s):
        if not ch.isspace():
            if not ch.isalpha():
                return False
            break
    # Todas las demás letras (salvo la primera letra encontrada) deben ser minúsculas
    for idx, ch in enumerate(s):
        if ch.isalpha():
            if idx == first_alpha_index:
                continue
            if not ch.islower():
                return False
    return True


def consigue_y_valida(name) -> str: # type: ignore
    """Obtiene un nombre del usuario y lo valida repetidamente hasta que sea correcto.
    
    Args:
        name: Descripción del tipo de nombre a ingresar (ej: "nombre de pila")
        
    Returns:
        El nombre validado y limpio (sin espacios iniciales/finales)
    """
    nombre = input(f"Ingrese su {name}: ")
    while not is_valid_name(nombre):
        print(f"El {name} debe contener sólo letras y espacios en blanco; puede tener espacios iniciales, pero debe empezar y terminar en letra, además el primer carácter debe ser mayúscula y el resto minúsculas.")
        nombre = input(f"Vuelva a ingresar su {name}: ")
    # Devolvemos el nombre limpio (sin espacios iniciales/ finales)
    return nombre.strip()


def consigue_y_valida_edad(limite_inferior, limite_superior) -> int: # type: ignore
    """Obtiene la edad del usuario y la valida dentro de un rango específico.
    
    Args:
        limite_inferior: Edad mínima permitida
        limite_superior: Edad máxima permitida
        
    Returns:
        La edad validada del usuario
    """
    edad = int(input("Ingrese su edad: ")) # int es número entero
    while edad < limite_inferior or edad > limite_superior:
        print(f"Las edades permitidas deben estar entre {limite_inferior} y {limite_superior}")
        edad = int(input("Vuelva a ingresar su edad: "))
    print(f"Su edad es: {edad}")
    return edad


def obtener_numero_desde_teclado(mensaje: str = "Ingrese un número", limite_inferior: int | None = None, limite_superior: int | None = None) -> int: # type: ignore
    """Obtiene un número entero del usuario con validación.
    
    Args:
        mensaje: Mensaje a mostrar al solicitar el número
        limite_inferior: Límite mínimo permitido (opcional)
        limite_superior: Límite máximo permitido (opcional)
        
    Returns:
        El número ingresado y validado
        
    Raises:
        ValueError: Si el usuario ingresa un valor que no es número
    """
    while True:
        try:
            numero = int(input(f"{mensaje}: "))
            
            if limite_inferior is not None and numero < limite_inferior:
                print(f"El número debe ser mayor o igual a {limite_inferior}")
                continue
                
            if limite_superior is not None and numero > limite_superior:
                print(f"El número debe ser menor o igual a {limite_superior}")
                continue
                
            return numero
            
        except ValueError:
            print("Error: Debe ingresar un número entero válido")

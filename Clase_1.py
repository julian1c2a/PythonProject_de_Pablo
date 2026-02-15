# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

"""
- Hemos creado un repositorio en GitHub para este proyecto.
- Hemos puesto el plugin de GitHub Copilot para Python.
- Plan del curso:
    -- Python        Lenguaje de scripting
        -- Python para aprender a programar
            -- Variables
            -- Condicionales
            -- Ciclos
            -- Funciones
            -- Listas, tuplas y diccionarios
            -- Crear proyectos de consola:
                -- Calculadora
                -- Juegos de Adivinanzas
            -- Enfoque OOP
                -- Clases
            -- Crear algunos proyectos visuales:
                -- Juego de la Vida
                -- Juego 2D (Spaceship)
        -- Uso de Git y GitHub
        -- Uso de Bibliotecas y entornos virtuales (DJango)
        -- Uso de herramientas de desarrollo
        -- Usdo de bases de datos
    -- JavaScript    Lenguaje de scripting (embebido en páginas web)
        --- HTML           Lenguaje de las páginas web
        ---- CSS           Lenguaje de estilos para HTML
    *-- Lenguajes intermedios: C#, Java
    *-- Lenguajes de bajo nivel: C, C++, Rust
    --
"""

"""
Variables: Números, cadenas de texto, booleanos
Formas de Visualizar variables: print, input, input()
"""

def is_valid_name(s: str) -> bool:
    """Valida un nombre permitiendo espacios iniciales y finales,
    exige al menos una letra y sólo admite letras y espacios.
    Además asegura que el primer y último carácter no-blanco sean letras,
    de modo que no haya signos o dígitos después de la parte alfabética.
    """
    if s is None:
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

def consigue_y_valida(name) -> str:
    nombre = input(f"Ingrese su {name}: ")
    while not is_valid_name(nombre):
        print(f"El {name} debe contener sólo letras y espacios en blanco; puede tener espacios iniciales, pero debe empezar y terminar en letra, además el primer carácter debe ser mayúscula y el resto minúsculas.")
        nombre = input(f"Vuelva a ingresar su {name}: ")
    # Devolvemos el nombre limpio (sin espacios iniciales/ finales)
    return nombre.strip()

def consigue_y_valida_edad(limite_inferior,limite_superior) -> int:
    edad = int(input("Ingrese su edad: ")) # int es número entero
    while edad < limite_inferior or edad > limite_superior:
        print(f"Las edades permitidas deben estar entre {limite_inferior} y {limite_superior}")
        edad = int(input("Vuelva a ingresar su edad: "))
    print(f"Su edad es: {edad}")
    return edad

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    nombre = consigue_y_valida("nombre de pila")
    print(f"Hola {nombre}")
    apellido_1 =  consigue_y_valida("primer apellido")
    print(f"Hola {nombre} {apellido_1}")
    apellido_2 =   consigue_y_valida("segundo apellido")
    print(f"Hola {nombre} {apellido_1} {apellido_2}")

    edad = consigue_y_valida_edad(5,100)
    print(f"Su edad es: {edad}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

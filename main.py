"""
Ejemplo de obtención y validación de datos del usuario.
Demuestra el uso de funciones del módulo validaciones.
"""

from validaciones import consigue_y_valida, consigue_y_valida_edad # type: ignore

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

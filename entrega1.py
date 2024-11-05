# Regular expression operations
import re

# Diccionario para almacenar usuarios y contraseñas
usuarios = {}

# Función para validar la contraseña
def validar_contrasena(contrasena):
    # Verifica que la contraseña tenga al menos 8 caracteres, sea alfanumérica y contenga un símbolo especial
    if len(contrasena) < 8:
        return False
    if not re.search(r"[A-Za-z]", contrasena): # Verifica caracteres alfabeticos
        return False
    if not re.search(r"\d", contrasena): # Verifica digitos de 0 a 9
        return False
    if not re.search(r"[!@#$%^&*()_+]", contrasena): # Verifica simbolos especiales
        return False
    return True

# Función para registrar un nuevo usuario
def registrar_usuario():
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    contrasena = input("Ingrese la contraseña: ")

    # Validación de campos vacíos
    if not nombre or not apellido or not contrasena:
        print("Todos los campos son obligatorios. Intente de nuevo.")
        return
    
    # Validación de la contraseña
    if not validar_contrasena(contrasena):
        print("La contraseña debe tener al menos 8 caracteres, ser alfanumérica y contener al menos un símbolo especial.")
        return

    # Almacenar usuario y contraseña en el diccionario
    usuario = f"{nombre.lower()}.{apellido.lower()}"
    usuarios[usuario] = contrasena
    print(f"Usuario '{usuario}' registrado exitosamente.")

# Función para mostrar la información de todos los usuarios registrados
def mostrar_usuarios():
    if not usuarios:
        print("No hay usuarios registrados.")
    else:
        print("Usuarios registrados:")
        for usuario, contrasena in usuarios.items():
            print(f"Usuario: {usuario}, Contraseña: {contrasena}")

# Función para el login de un usuario
def login_usuario():
    usuario = input("Ingrese su nombre de usuario: ").lower()
    contrasena = input("Ingrese su contraseña: ")
    
    # Comprobación de usuario y contraseña
    if usuario in usuarios and usuarios[usuario] == contrasena:
        print(f"Bienvenido, {usuario}. Login exitoso.")
    else:
        print("Usuario o contraseña incorrectos.")

# Programa principal
def menu():
    while True:
        print("\nSeleccione una opción:")
        print("1. Registrar usuario")
        print("2. Mostrar usuarios")
        print("3. Login")
        print("4. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            mostrar_usuarios()
        elif opcion == "3":
            login_usuario()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el menú
menu()

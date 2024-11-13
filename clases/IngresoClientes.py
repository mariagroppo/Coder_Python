# Clase que maneja el registro y login de clientes

from clases.Cliente import Cliente

class IngresoClientes:
    def __init__(self):
        self.usuarios = {}

    def registrar_usuario(self):
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        correo = input("Ingrese el correo electrónico: ")
        contrasena = input("Ingrese la contraseña: ")

        # Validación de campos vacíos
        if not nombre or not apellido or not correo or not contrasena:
            print("Todos los campos son obligatorios. Intente de nuevo.")
            return

        cliente = Cliente(nombre, apellido, correo, contrasena)

        # Validación de la contraseña
        if not cliente.validar_contrasena():
            print("La contraseña debe tener al menos 8 caracteres, ser alfanumérica y contener al menos un símbolo especial.")
            return

        # Almacenar usuario y contraseña en el diccionario
        usuario = f"{nombre.lower()}.{apellido.lower()}"
        self.usuarios[usuario] = cliente
        print(f"{cliente} registrado exitosamente.")

    def mostrar_usuarios(self):
        if not self.usuarios:
            print("No hay usuarios registrados.")
        else:
            print("Usuarios registrados:")
            for usuario, cliente in self.usuarios.items():
                print(f"Username: {usuario}, Nombre: {cliente}")

    def login_usuario(self):
        usuario = input("Ingrese su nombre de usuario: ").lower()
        contrasena = input("Ingrese su contraseña: ")

        # Comprobación de usuario y contraseña
        if usuario in self.usuarios and self.usuarios[usuario].contrasena == contrasena:
            print(f"Bienvenido, {self.usuarios[usuario].nombre}. Login exitoso.")
        else:
            print("Usuario o contraseña incorrectos.")
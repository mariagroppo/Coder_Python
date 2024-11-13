import re

# Clase Cliente
class Cliente:
    # Atributos: nombre, apellido, correo, y contrasena
    def __init__(self, nombre, apellido, correo, contrasena):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.contrasena = contrasena

    # Metodo: Devuelve una representación en cadena del cliente, mostrando su nombre completo
    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}"

    # Metodo: Valida contrasena
    def validar_contrasena(self):
        if len(self.contrasena) < 8:
            return False
        if not re.search(r"[A-Za-z]", self.contrasena):
            return False
        if not re.search(r"\d", self.contrasena):
            return False
        if not re.search(r"[!@#$%^&*()_+]", self.contrasena):
            return False
        return True
    

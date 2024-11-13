from  clases.IngresoClientes import IngresoClientes

# Programa principal
def menu():
    sistema = IngresoClientes()
    while True:
        print("\nSeleccione una opción:")
        print("1. Registrar usuario")
        print("2. Mostrar usuarios")
        print("3. Login")
        print("4. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            sistema.registrar_usuario()
        elif opcion == "2":
            sistema.mostrar_usuarios()
        elif opcion == "3":
            sistema.login_usuario()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el menú
menu()

max_intentos = 3

def main():
    pin_correcto = 1234
    intentos = 0
    acceso = False

    while intentos < max_intentos and not acceso:
        try:
            pin_tecleado = int(input(f"PIN (intento {intentos + 1}): "))
        except ValueError:
            print("Escribe un número entero.")
            continue

        intentos = intentos + 1

        if pin_tecleado == pin_correcto:
            acceso = True

    if acceso:
        mensaje = "Acceso"
    else:
        mensaje = "Denegado"

    print(mensaje)


if __name__ == "__main__":
    main()







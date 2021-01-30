def enumeracion():
    objetivo = int(input('Escribe un entero: '))
    respuesta = 0

    while respuesta ** 2 < objetivo:
        respuesta += 1

    if respuesta ** 2 == objetivo:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene una raiz cuadrada exacta')

def binaria():
    objetivo = int(input('Escribe un numero: '))
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0 , objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) / 2

    print(f'La raiz cuadrada de {objetivo} es {respuesta}')

def aproximacion():
    objetivo = int(input('Escribe un numero: '))
    epsilon = 0.01
    paso = epsilon ** 2
    respuesta = 0.0

    while abs(respuesta **2 - objetivo) >=epsilon and respuesta <= objetivo:
        respuesta += paso

    if abs(respuesta **2 - objetivo) >= epsilon:
        print(f'No se encontro la raiz cuadrada {objetivo}')
    else:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')

def menu():
    print("""Elige una opcion para calcular la raiz cuadrada:
    1 .- Enumeracion exahustiva
    2 .- Aproximacion
    3 .- Busqueda binaria
    """)

def run():
    opcion = int(input(menu()))

    if opcion == 1:
        enumeracion()

    elif opcion == 2:
        aproximacion()

    elif opcion == 3:
        binaria()

    else:
        print("Elige una opcion valida.")
        run()


if __name__ == "__main__":
    run()
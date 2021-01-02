def run():
    nombre = input('Escribe tu nombre: ')
    saludo = f'Hola, Bienvenido {nombre}'
    print(saludo, f'. La longitud del string es de :{len(saludo)}')


if __name__ == '__main__':
    run()
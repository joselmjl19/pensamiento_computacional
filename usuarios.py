def run():
    nombre_usuario1 = input('Ingresa el nombre del primer usuario: ')
    edad_usuario1 = int(input('Ingresa la edad del primer usuario: '))
    nombre_usuario2 = input('Ingresa el nombre del segundo usuario: ')
    edad_usuario2 = int(input('Ingresa la edad del segundo usuario: '))

    if edad_usuario1 > edad_usuario2:
        print(f'El usuario {nombre_usuario1} es mayor que el usuario {nombre_usuario2}')
    elif edad_usuario1 < edad_usuario2:
        print(f'El usuario {nombre_usuario2} es mayor que el usuario {nombre_usuario1}')
    else:
        print('Ambos usuarios tienen la misma edad')


if __name__ == '__main__':
    run()
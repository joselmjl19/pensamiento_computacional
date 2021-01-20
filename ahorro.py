import random

def run():
    n = 365
    numero = []

    for i in range(n):
        numero.append(i+1)

    random.shuffle(numero,random.random)
    
    print(numero)
    

if __name__ == '__main__':
    run() 
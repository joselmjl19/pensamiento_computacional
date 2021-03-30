def run():
    def factorial(n):
        """Calcula el factorial de n
        n int > 0 
        retuns n! 
        """
        if n == 1:
            return 1

        return n * factorial(n - 1)

    n = int(input("Ingresa un numero entero mayor a 1: "))
    print(factorial(n))

if __name__ == '__main__':
    run()
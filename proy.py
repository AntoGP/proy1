from modulo import *


opcion = 1
while opcion !=11:
    print("MENU")
    print("[1] Triangulo con numeros ")
    print("[2] Triangulo invertido")
    print("[3] Piramide de Asteriscos")
    print("[4] Piramide de numeros")
    print("[5] Deletreando numeros")
    print("[6] Codigo de barras")
    print("[7] Letra Z")
    print("[8] Siguiente Primo")
    print("[9] Sumar dos numeros")
    print("[10] funcion 10 - libre que implique el uso de bucles anidados y llamada a funciones")
    print("[11] FIN")
    opcion = int(input("Selecciona una opcion: "))
    while opcion <1 or opcion >11:
        opcion = int(input("Selecciona una opcion: "))
    #---- se ejecuta la opcion
    print("------------------------------------")
    if opcion == 1:
        print("Opcion 1")
        #--- leer datos e invocar a la funcion 1
        filas = int(input("Filas [1-9]:"))
        while filas<1 or filas>9:
            filas = int(input("Filas [1-9]:"))
        print()
        print( trianguloConNumeros(filas))

    elif opcion == 2:
        print("Opcion 2")
        # --- leer datos e invocar a la funcion
        filas = int(input("Filas [1-9]:"))
        while filas < 1 or filas > 9:
            filas = int(input("Filas [1-9]:"))
        print()
        print(trianguloInvertido(filas))
    elif opcion == 3:
        print("Opcion 3")
        # --- leer datos e invocar a la funcion
        filas = int(input("Filas [1-15]:"))
        while filas < 1 or filas > 16:
            filas = int(input("Filas [1-15]:"))
        print()
        print(piramideDeAsteriscos(filas))
    elif opcion == 4:
        print("Opcion 4")
        # --- leer datos e invocar a la funcion
        filas = int(input("Filas [1-15]:"))
        while filas < 1 or filas > 16:
            filas = int(input("Filas [1-15]:"))
        print()
        print(piramideDeNumeros(filas))

    elif opcion == 5:
        print("Opcion 5")
        # --- leer datos e invocar a la funcion
        numero = int(input("Numero de al menos 3 digitos:"))
        while numero <100:
            numero = int(input("Numero de al menos 3 digitos:"))
        print( deletrearNumero(numero))

    elif opcion == 6:
        print("Opcion 6")
        # --- leer datos e invocar a la funcion
        numero = int(input("Numero de al menos 3 digitos:"))
        while numero < 100:
            numero = int(input("Numero de al menos 3 digitos:"))
        print(codigoDeBarras(numero))

    elif opcion == 7:
        print("Opcion 7")
        # --- leer datos e invocar a la funcion
        filas = int(input("Filas >= 3:"))
        while filas <3:
            filas = int(input("Filas >= 3:"))
        print( dibujarLaZ(filas))

    elif opcion == 8:
        print("Opcion 8")
        # --- leer datos e invocar a la funcion
        numero = int(input("Numero > 1:"))
        while numero <=1:
            numero = int(input("Numero > 1:"))
        print( siguientePrimo(numero))

    elif opcion == 9:
        # --- leer datos e invocar a la funcion
        n1 = input("Numero 1 - Expresa en palabras cada digito : ")
        n2 = input("Numero 2 - Expresa en palabras cada digito : ")
        print(sumarDosNumeros(n1, n2))
    elif opcion == 10:
        print("Opcion 10")
        print("8. siguientePrimo")
        print(siguientePrimo(45))
        print(siguientePrimo(733))
        print(siguientePrimo(15))
        print(siguientePrimo(941))
        print()

        print("10. funcion10")
        print(funcion10(3))
        print()
        print(funcion10(5))
        print()
        print(funcion10(9))
    print("------------------------------------")
print("Gracias por usar el programa")

def trianguloConNumeros(filas):
    resultado = ""

    for i in range(1, filas + 1):
        resultado += " " * (filas - i)
        for j in range(1, i + 1):
            resultado += str(j)
        resultado += "\n"

    return resultado

def trianguloInvertido(filas):
    resultado = ""

    for i in range(filas, 0, -1):
        for j in range(i):
            resultado += str(i)
        resultado += "\n"

    return resultado



def piramideDeAsteriscos(filas):
    resultado = ""
    for i in range(1, filas + 1):
        linea = ""
        for e in range(filas - i):
            linea = linea + " "
        for a in range(2 * i - 1):
            linea = linea + "*"
        if i == 1:
            resultado = linea
        else:
            resultado = resultado + "\n" + linea
    return resultado


def piramideDeNumeros(filas):
    resultado = ""

    for fila in range(1, filas + 1):

        for espacio in range(filas - fila):
            resultado = resultado + " "

        for numero in range(1, 2 * fila):
            resultado = resultado + str(numero % 10)

        if fila < filas:
            resultado = resultado + "\n"

    return resultado


def deletrearNumero(numero):
    resultado = ""

    for digito in str(numero):
        if digito == "0":
            resultado = resultado + "cero "
        elif digito == "1":
            resultado = resultado + "uno "
        elif digito == "2":
            resultado = resultado + "dos "
        elif digito == "3":
            resultado = resultado + "tres "
        elif digito == "4":
            resultado = resultado + "cuatro "
        elif digito == "5":
            resultado = resultado + "cinco "
        elif digito == "6":
            resultado = resultado + "seis "
        elif digito == "7":
            resultado = resultado + "siete "
        elif digito == "8":
            resultado = resultado + "ocho "
        elif digito == "9":
            resultado = resultado + "nueve "

    return resultado


def codigoDeBarras(numero):
    texto = str(numero)
    resultado = ""
    for i in range(len(texto)):
        digito = int(texto[i])
        if digito == 0:
            codigo = "#"
        else:
            codigo = ""
            for k in range(digito):
                codigo = codigo + "I"
        if i == 0:
            resultado = codigo
        else:
            resultado = resultado + " " + codigo
    return resultado

def dibujarLaZ(filas):
    resultado = ""

    for i in range(filas):
        if i == 0 or i == filas - 1:
            resultado += "*" * filas
        else:
            espacios = filas - 1 - i
            resultado += " " * espacios + "*"

        resultado += "\n"

    return resultado

def siguientePrimo(numero):
    numero += 1

    while True:
        es_primo = True

        for i in range(2, numero):
            if numero % i == 0:
                es_primo = False
                break

        if es_primo:
            return numero

        numero += 1

def sumarDosNumeros(n1, n2):
    palabras = {
        "cero": "0", "uno": "1", "dos": "2", "tres": "3", "cuatro": "4",
        "cinco": "5", "seis": "6", "siete": "7", "ocho": "8", "nueve": "9"
    }

    numero1 = ""
    numero2 = ""

    for palabra in n1.split():
        numero1 += palabras[palabra]

    for palabra in n2.split():
        numero2 += palabras[palabra]

    suma = int(numero1) + int(numero2)

    return deletrearNumero(suma)

def funcion10(filas: int) -> str:
    if type(filas) != int or filas < 1 or filas > 9:
        return "Error: filas debe ser un entero entre 1 y 9"
    resultado: str = ""
    primo: int = 1
    for fila in range(1, filas + 1):
        contenido: str = ""
        for columna in range(fila):
            primo = siguientePrimo(primo)
            contenido = contenido + str(primo) + " "
        if fila > 1:
            resultado = resultado + "\n"
        resultado = resultado + contenido.strip()
    return resultado

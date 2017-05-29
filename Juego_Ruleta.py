"""
TRABAJO PRÁCTICO Nº 1 - EL JUEGO DE LA RULETA - ALGORITMOS Y ESTRUCTURAS DE DATOS

MATEO VERDAGUER - 72310
MARCOS JAVIER MARIN - 75695
"""

import random


def paridad(n):
    if n % 2 == 0:
        par = True
    else:
        par = False
    return par


def colores(n, par):
    negro = rojo = False

    if 0 < n <= 10:  # 1 al 10 impares rojos y pares negros
        if par:
            negro = True
        else:
            rojo = True
    if 10 < n <= 18:  # 11 al 18 impares negros y pares rojos
        if par:
            rojo = True
        else:
            negro = True
    if 18 < n <= 28:  # 19 al 28 impares rojos y pares negros
        if par:
            negro = True
        else:
            rojo = True
    if 28 < n <= 36:  # 29 al 36 impares negros y pares rojos
        if par:
            rojo = True
        else:
            negro = True
    return negro, rojo


def pf(n):
    pasa = falta = False
    if 0 < n <= 18:
        falta = True
    elif 18 < n <= 36:
        pasa = True
    return pasa, falta


def docenas(n):
    docena = 0

    if 0 < n < 13:
        docena = 1
    elif 12 < n <= 24:
        docena = 2
    elif 24 < n <= 36:
        docena = 3
    return docena


def columnas(n):
    columna = 0
    columna1 = 1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34
    columna2 = 2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35
    columna3 = 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36

    if n in columna1:
        columna = 1
    elif n in columna2:
        columna = 2
    elif n in columna3:
        columna = 3
    return columna


# ---------------------------------------------------------------------------------------------------------------------
# Comienzo del programa

def main():

    opcion = 0
    usada1 = usada2 = usada3 = usada4 = usada5 = usada6 = False
    apuesta_pleno = apuesta_color = apuesta_paridad = apuesta_pf = apuesta_columna = apuesta_docena = False
    recupera = gana = 0
    aposto = False
    mejor_jugada = peor_jugada = fichas_jugada = fichas_mejor_jugada = fichas_peor_jugada = 0
    numero_ruleta = random.randint(0, 37)
    numero = 0
    jugada = 1

    print("JUEGO DE LA RULETA")

    print("_" * 40)

    fichas = int(input("Ingrese la cantidad de fichas que posee: "))

    while opcion != 8:
        print("_" * 60)
        print("Menu:")
        print("1- Apostar Rojo/Negro")
        print("2- Apostar Par/Impar")
        print("3- Apostar Pasa/Falta")
        print("4- Apostar Columna")
        print("5- Apostar Docena")
        print("6- Apostar Pleno")
        print("7- No va más!")
        print("8- Salir")
        print("_" * 60)
        opcion = int(input("\n Ingrese su opcion: "))

        # Apuesta 1 - Rojo / Negro
        if opcion == 1:
            if not usada1:
                color = int(input("\n Ingrese 1 si elige Negro o 2 si elige Rojo: "))
                apuesta1 = int(input("Cuantas fichas desea apostar a esta categoria? "))
                while fichas - apuesta1 < 0:
                    apuesta1 = int(input("No posee tantas fichas,vuelva a ingresar cuantas fichas desea "
                                         "apostar a esta categoria: "))
            else:
                apuesta1 = int(input("Ya aposto a esta categoria, cuantas fichas mas desea agregar? "))
                while fichas - apuesta1 < 0:
                    apuesta1 = int(input("No posee tantas fichas,vuelva a ingresar cuantas fichas desea "
                                         "apostar a esta categoria: "))
            usada1 = True
            fichas -= apuesta1
            apuesta_color = True
            aposto = True

            # Apuesta 2 - Par / Impar
        if opcion == 2:
            if not usada2:
                par_impar = int(input("\n Ingrese 1 si elige Par o 2 si elige Impar: "))
                apuesta2 = int(input("Cuantas fichas desea apostar a esta categoria?: "))
                while fichas - apuesta2 < 0:
                    apuesta2 = int(input("No posee tantas fichas,vuelva a ingresar cuantas fichas desea "
                                         "apostar a esta categoria: "))
            else:
                apuesta2 = int(input("Ya aposto a esta categoria, cuantas fichas mas desea agregar? "))
                while fichas - apuesta2 < 0:
                    apuesta2 = int(input("No posee tantas fichas,vuelva a ingresar cuantas fichas desea "
                                         "apostar a esta categoria: "))
            usada2 = True
            fichas -= apuesta2
            apuesta_paridad = True
            aposto = True

            # Apuesta 3 - Pasa / Falta
        if opcion == 3:
            if not usada3:
                pasa_falta = int(input("\n Ingrese 1 si elige Pasa o 2 si elige Falta: "))
                apuesta3 = int(input("Cuantas fichas desea apostar a esta categoria? "))
                while fichas - apuesta3 < 0:
                    apuesta3 = int(input("No posee tantas fichas,vuelva a ingresar cuantas fichas desea "
                                         "apostar a esta categoria: "))
            else:
                apuesta3 = int(input("Ya aposto a esta categoria, cuantas fichas mas desea agregar? "))
                while fichas - apuesta3 < 0:
                    apuesta3 = int(input("No posee tantas fichas,vuelva a ingresar cuantas fichas desea "
                                         "apostar a esta categoria: "))
            usada3 = True
            fichas -= apuesta3
            apuesta_pf = True
            aposto = True

            # Apuesta 4 - Columna
        if opcion == 4:
            if not usada4:
                columna_usuario = int(input("\n Ingrese 1 si elige la primera columna, 2 si elige la segunda o 3 si"
                                            " elige la tercera:"))
                apuesta4 = int(input("Cuantas fichas desea apostar a esta categoria? "))
                while fichas - apuesta4 < 0:
                    apuesta4 = int(input("No posee tantas fichas,vuelva a ingresar cuantas fichas desea "
                                         "apostar a esta categoria: "))
            else:
                apuesta4 = int(input("Ya aposto a esta categoria, cuantas fichas mas desea agregar? "))
                while fichas - apuesta4 < 0:
                    apuesta4 = int(input("No posee tantas fichas,vuelva a ingresar cuantas fichas desea "
                                         "apostar a esta categoria: "))
            usada4 = True
            fichas -= apuesta4
            apuesta_columna = True
            aposto = True

            # Apuesta 5 - Docena
        if opcion == 5:
            if not usada5:
                docena_usuario = int(input("\n Ingrese 1 si elige la primera docena, 2 si elige la segunda o 3 si "
                                           "elige la tercera: "))
                apuesta5 = int(input("Cuantas fichas desea apostar a esta categoria? "))
                while fichas - apuesta5 < 0:
                    apuesta5 = int(input("No posee tantas fichas,vuelva a ingresar cuantas fichas desea "
                                         "apostar a esta categoria: "))
            else:
                apuesta5 = int(input("Ya aposto a esta categoria, cuantas fichas mas desea agregar? "))
                while fichas - apuesta5 < 0:
                    apuesta5 = int(input("No posee tantas fichas,vuelva a ingresar cuantas fichas desea "
                                         "apostar a esta categoria: "))
            usada5 = True
            fichas -= apuesta5
            apuesta_docena = True
            aposto = True

            # Apuesta 6 - Pleno
        if opcion == 6:
            if not usada6:
                numero = int(input("Ingrese el numero al que desea apostar: "))
                apuesta6 = int(input("Cuantas fichas desea apostar a esta categoria? "))
                while fichas - apuesta6 < 0:
                    apuesta6 = int(input("No posee tantas fichas,vuelva a ingresar cuantas fichas desea "
                                         "apostar a esta categoria: "))
            else:
                apuesta6 = int(input("Ya aposto a esta categoria, cuantas fichas mas desea agregar? "))
                while fichas - apuesta6 < 0:
                    apuesta6 = int(input("No posee tantas fichas,vuelva a ingresar cuantas fichas desea "
                                         "apostar a esta categoria: "))
            usada6 = True
            fichas -= apuesta6
            apuesta_pleno = True
            aposto = True

            # No va mas!
        if opcion == 7:

            if aposto:

                # Se establecen las caracteristicas en base al numero obtenido

                jugada += 1

                # Par - Impar
                par = paridad(numero_ruleta)

                # Rojo - Negro
                negro, rojo = colores(numero_ruleta, par)

                # Pasa - Falta
                pasa, falta = pf(numero_ruleta)

                # Docenas
                docena = docenas(numero_ruleta)

                # Columnas
                columna = columnas(numero_ruleta)

                # -----------------------------------------------------------------------------------------------------
                # Se procede a comparar el numero obtenido con las apuestas del usuario

                # Pleno
                if apuesta_pleno:
                    if numero_ruleta == numero:
                        recupera = 1
                        gana = 35
                        fichas = fichas + 36

                # Color
                if apuesta_color:
                    if color == 1 and negro:
                        recupera = recupera + 1
                        gana = gana + 1
                        fichas = fichas + 2
                    elif color == 2 and rojo:
                        recupera = recupera + 1
                        gana = gana + 1
                        fichas = fichas + 2

                # Paridad
                if apuesta_paridad:
                    if par_impar == 1 and par:
                        recupera = recupera + 1
                        gana = gana + 1
                        fichas = fichas + 2
                    elif par_impar == 2 and par is False:
                        recupera = recupera + 1
                        gana = gana + 1
                        fichas = fichas + 2

                # Pasa / Falta
                if apuesta_pf:
                    if pasa_falta == 1 and pasa:
                        recupera = recupera + 1
                        gana = gana + 1
                        fichas = fichas + 2
                    elif pasa_falta == 2 and falta:
                        recupera = recupera + 1
                        gana = gana + 1
                        fichas = fichas + 2

                # Docenas
                if apuesta_docena:
                    if docena_usuario == 1 and docena == 1:
                        recupera = recupera + 1
                        gana = gana + 2
                        fichas = fichas + 3
                    elif docena_usuario == 2 and docena == 2:
                        recupera = recupera + 1
                        gana = gana + 2
                        fichas = fichas + 3
                    elif docena_usuario == 3 and docena == 3:
                        recupera = recupera + 1
                        gana = gana + 2
                        fichas = fichas + 3

                # Columnas
                if apuesta_columna:
                    if columna_usuario == 1 and columna == 1:
                        recupera = recupera + 1
                        gana = gana + 2
                        fichas = fichas + 3
                    elif columna_usuario == 2 and columna == 2:
                        recupera = recupera + 1
                        gana = gana + 2
                        fichas = fichas + 3
                    elif columna_usuario == 3 and columna == 3:
                        recupera = recupera + 1
                        gana = gana + 2
                        fichas = fichas + 3

                print("fichas", fichas)
                if jugada == 1:
                    fichas_jugada = gana

                # -----------------------------------------------------------------------------------------------------
                # Se identifica la mejor y la peor jugada

                if gana > fichas_jugada:
                    mejor_jugada = jugada
                    fichas_mejor_jugada = gana
                if gana <= fichas_jugada:
                    peor_jugada = jugada
                    fichas_peor_jugada = gana

            else:
                print("NO HA REALIZADO NINGUNA APUESTA.")

            print("_" * 60)
            print("\n JUGADA TERMINADA")

    # -----------------------------------------------------------------------------------------------------------------
    # Calculo del dinero ganado
    dinero = fichas * 100
    comision = (dinero * 5) / 100
    dinero = dinero - comision

    print("\n")
    print("_" * 40)
    print("NUMERO OBTENIDO EN LA RULETA: ", numero_ruleta)
    print("\n FICHAS DEL JUGADOR:", fichas)
    print("\n RECUPERO ", recupera, "FICHAS.")
    print("\n GANO: ", gana, "FICHAS.")
    print("\n DINERO: $", dinero)
    print("\n LA MEJOR JUGADA FUE LA", mejor_jugada, "GANANDO ", fichas_mejor_jugada, "FICHAS.")
    print("\n LA PEOR JUGADA FUE LA", peor_jugada, "GANANDO ", fichas_peor_jugada, "FICHAS.")

main()

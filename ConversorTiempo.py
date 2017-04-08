__author__ = "Mateo Verdaguer"

print("CONVERSION DE UNIDADES DE TIEMPO")


problem_selec = int(input("Ingrese 1 si desea convertir de (hh:mm:ss) a segundos, o ingrese 2 si desea convertir "
                          "de segundos a (hh:mm:ss): "))

while problem_selec > 2 or problem_selec < 0:
    problem_selec = int(input("Ingrese 1 si desea convertir de (hh:mm:ss) a segundos, o ingrese 2 si desea convertir "
                              "de segundos a (hh:mm:ss): "))

if problem_selec == 1:
    print("CONVERSOR DE HH:MM:SS A SEGUNDOS")

    horas = int(input("Ingrese las horas: "))
    minutos = int(input("Ingrese los minutos: "))
    segundos = int(input("Ingrese los segundos: "))

    horas_sec = horas * 3600
    minutos_sec = minutos * 60

    total_segundos = horas_sec + minutos_sec + segundos

    print(total_segundos)

elif problem_selec == 2:
    print("CONVERSOR DE SEGUNDOS A HH:MM:SS")

    segundos_totales = int(input("Ingrese el tiempo total en segundos: "))

    horas = segundos_totales // 3600
    minutos = (segundos_totales % 3600) // 60
    segundos = segundos_totales % 60

    print(horas)
    print(minutos)
    print(segundos)

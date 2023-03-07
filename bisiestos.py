# **************************************************************************** #
#                                                                              #
#                                                         .-------------.      #
#                                                         |.-----------.|      #
#                                                         ||           ||      #
#                                                         ||  Jkutkut  ||      #
#    bisiestos.py                                         ||           ||      #
#                                                         |'-----------'|      #
#    By: Jkutkut  https://github.com/jkutkut              /:::::::::::::\      #
#                                                        /:::::::::::::::\     #
#    Created: 2023/03/07 08:46:34 by Jkutkut            /:::===========:::\    #
#    Updated: 2023/03/07 09:05:06 by Jkutkut            '-----------------'    #
#                                                                              #
# **************************************************************************** #

from tools.ask import askInt

def es_bisiesto(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0;

def numbisiestos(y1: int, y2: int) -> tuple:
    bisiestos: int = 0
    for y in range(y1, y2 + 1):
        if es_bisiesto(y):
            bisiestos += 1
    # Optimización para calcular los días
    days = (y2 - y1 + 1) * 365 + bisiestos
    return (bisiestos, days)

if __name__ == "__main__":
    '''
    Escribe un programa en Python llamado bisiestos.py que cree una función
    llamada numbisiestos() a la que se le pasan dos años.
    La función tendrá que calcular el número de años bisiestos que hay entre
    esos dos años (incluyendo los dos años) y el número de días total entre
    esos dos años (incluyendo los dos años).
    El programa pedirá al usuario que introduzca los dos años y mostrará en la
    consola el resultado de la comprobación.

    Crea una función llamada es_bisiesto() que calcule si un año es bisiesto o
    no sabiendo que los años bisiestos son múltiplos de 4.
    Si un año es divisible entre 4 pero no entre 100, entonces SÍ es un año
    bisiesto. Si un año es divisible entre 100 y 400, entonces SÍ es un año
    bisiesto. Si un año es divisible entre 100 pero no entre 400, entonces NO
    es un año bisiesto. En otros casos, tampoco.

    La salida por consola será de la forma:
        Dame un año:   1800 
        Dame otro año: 1900 
        Entre 1800 y 1900 (ambos incluidos) hubo/hay/habrá 24 años bisiestos
        y un total de 36889 días. 
    '''
    y1 = askInt("Dame un año: ", 0)
    y2 = askInt("Dame otro: ", y1 + 1)

    r = numbisiestos(y1, y2)
    print(f"Entre {y1}, {y2} (ambos incluidos) hubo/hay/habrá {r[0]}", end = "")
    print(f" años bisiestos y un total de {r[1]} días. ")

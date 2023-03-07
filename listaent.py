# **************************************************************************** #
#                                                                              #
#                                                         .-------------.      #
#                                                         |.-----------.|      #
#                                                         ||           ||      #
#                                                         ||  Jkutkut  ||      #
#    listaent.py                                          ||           ||      #
#                                                         |'-----------'|      #
#    By: Jkutkut  https://github.com/jkutkut              /:::::::::::::\      #
#                                                        /:::::::::::::::\     #
#    Created: 2023/03/07 08:40:54 by Jkutkut            /:::===========:::\    #
#    Updated: 2023/03/07 09:07:07 by Jkutkut            '-----------------'    #
#                                                                              #
# **************************************************************************** #

from tools.ask import askInt

if __name__ == '__main__':
    '''
    Escribe un programa en Python llamado listaent.py que pida dos números
    enteros n1 y n2 al usuario y muestre por consola una lista de n2 números
    consecutivos a partir de n1. Los números serán enteros positivos.
    Si n2 es cero no se generará ninguna lista. El programa controlará los
    casos negativos que no cumplan los criterios establecidos.
    Por ejemplo, la salida por consola, según el caso, sería de la forma: 

    Dame el número entero inicial: 4 
    Dime cuántos valores quieres: 10 

    Resultado: [4, 5, 6, 7, 8, 9, 10, 11, 12, 13] 
    -----------------------------------------------------------------------
    Dame el número entero inicial: 4 
    Dime cuántos valores quieres: -5 

    Resultado: ¡La cantidad de valores no puede ser negativa! 
    -----------------------------------------------------------------------
    Dame el número entero inicial: 4 
    Dime cuántos valores quieres: 0 

    Resultado: 
    '''
    n1 = askInt("Dame el número entero inicial: ", 0)
    n2 = askInt("Dime cuántos valores quieres: ", 0)

    r = [i for i in range(n1, n1 + n2)]
    r = r if len(r) > 0 else ""
    print(f"Resultado:\t\t{r}")

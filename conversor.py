# **************************************************************************** #
#                                                                              #
#                                                         .-------------.      #
#                                                         |.-----------.|      #
#                                                         ||           ||      #
#                                                         ||  Jkutkut  ||      #
#    conversor.py                                         ||           ||      #
#                                                         |'-----------'|      #
#    By: Jkutkut  https://github.com/jkutkut              /:::::::::::::\      #
#                                                        /:::::::::::::::\     #
#    Created: 2023/03/07 09:46:39 by Jkutkut            /:::===========:::\    #
#    Updated: 2023/03/07 11:05:06 by Jkutkut            '-----------------'    #
#                                                                              #
# **************************************************************************** #

from moneyconversor.app import MoneyConversorApp

if __name__ == '__main__':
    '''
    Crea un programa en Python llamado Conversor.py que cree una ventana con
    Tkinter para convertir valores monetarios entre divisas Euro–Dólar y
    viceversa.
    1. La ventana llevará el título ‘Conversor Euro – Dólar USA’ y una imagen
    como logo de la aplicación.
    2. Se introducirá una cantidad de dinero, se indicará de qué divisa se trata
    y se convertirá a la otra divisa.
    3. La ventana tendrá una etiqueta principal centrada en la parte superior
    de la ventana cuyo texto será ‘Conversión de divisas Euro - Dólar USA’.
    4. Abajo, habrá una etiqueta cuyo texto será Cantidad a convertir. A su
    derecha se introducirá un Cuadro de texto para escribir la cantidad de
    dinero a convertir a la otra divisa.
    5. Debajo, habrá una etiqueta con texto ‘Conversión’ y 2 radiobutton
    que permitan seleccionar a qué divisa se quiere convertir la cantidad
    indicada. Esta conversión será de Euro a Dólar USA o de Dólar USA a Euro.
    6. Los cambios que se aplican en marzo de 2023 son los siguientes:
    1 dólar USA = 0,947983 euros         1 Euro = 1,054883 Dólares USA
    7. Se introducirá un botón con texto Convertir que realizará el cambio de
    divisa requerido y mostrará el resultado en otra etiqueta. Habrá una
    etiqueta con texto “Valor de la conversión” y a su derecha otra etiqueta
    donde se indicará el resultado numérico del cambio y en qué divisa se ha
    convertido.
    8. Una vez que tengas la ventana ajustada a su contenido, no permitas que
    se pueda redimensionar.

    Nota: Por motivos de diseño, la interfaz se ha modificado ligeramente.
    Sin embargo, toda la funcionalidad y elementos utilizados son los mismos.
    '''
    MoneyConversorApp().run()

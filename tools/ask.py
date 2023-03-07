# **************************************************************************** #
#                                                                              #
#                                                         .-------------.      #
#                                                         |.-----------.|      #
#                                                         ||           ||      #
#                                                         ||  Jkutkut  ||      #
#    ask.py                                               ||           ||      #
#                                                         |'-----------'|      #
#    By: Jkutkut  https://github.com/jkutkut              /:::::::::::::\      #
#                                                        /:::::::::::::::\     #
#    Created: 2023/03/07 08:51:37 by Jkutkut            /:::===========:::\    #
#    Updated: 2023/03/07 08:51:45 by Jkutkut            '-----------------'    #
#                                                                              #
# **************************************************************************** #

def askInt(question: str, minimum = None, maximum = None) -> float:
    while True:
        try:
            nbr = int(input(question))
            if minimum != None and nbr < minimum:
                print("El valor tiene que ser mayor que", minimum)
                continue
            elif maximum != None and nbr > maximum:
                print("El valor tiene que ser menor que", maximum)
                continue
            return nbr
        except ValueError:
            print("El valor tiene que ser un número entero.")

# **************************************************************************** #
#                                                                              #
#                                                         .-------------.      #
#                                                         |.-----------.|      #
#                                                         ||           ||      #
#                                                         ||  Jkutkut  ||      #
#    radiobutton.py                                       ||           ||      #
#                                                         |'-----------'|      #
#    By: Jkutkut  https://github.com/jkutkut              /:::::::::::::\      #
#                                                        /:::::::::::::::\     #
#    Created: 2023/03/02 14:11:45 by Jkutkut            /:::===========:::\    #
#    Updated: 2023/03/07 10:12:41 by Jkutkut            '-----------------'    #
#                                                                              #
# **************************************************************************** #

import tkinter

from moneyconversor.style import ConversorStyle as STYLE

class Radiobutton(tkinter.Radiobutton):
    def __init__(self, window, text, value, variable):
        super().__init__(
            window,
            text = text,
            value = value,
            variable = variable,
            bg = STYLE.BG,
            fg = STYLE.FG,
            highlightthickness = 0
        )

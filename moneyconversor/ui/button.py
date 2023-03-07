# **************************************************************************** #
#                                                                              #
#                                                         .-------------.      #
#                                                         |.-----------.|      #
#                                                         ||           ||      #
#                                                         ||  Jkutkut  ||      #
#    button.py                                            ||           ||      #
#                                                         |'-----------'|      #
#    By: Jkutkut  https://github.com/jkutkut              /:::::::::::::\      #
#                                                        /:::::::::::::::\     #
#    Created: 2023/03/02 14:11:45 by Jkutkut            /:::===========:::\    #
#    Updated: 2023/03/07 10:12:21 by Jkutkut            '-----------------'    #
#                                                                              #
# **************************************************************************** #

import tkinter

from moneyconversor.style import ConversorStyle as STYLE

class Button(tkinter.Button):
    def __init__(self, window, text):
        super().__init__(
            window,
            text = text,
            highlightbackground = STYLE.BG,
            highlightcolor = STYLE.FG,
        )

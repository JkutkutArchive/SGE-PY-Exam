# **************************************************************************** #
#                                                                              #
#                                                         .-------------.      #
#                                                         |.-----------.|      #
#                                                         ||           ||      #
#                                                         ||  Jkutkut  ||      #
#    label.py                                             ||           ||      #
#                                                         |'-----------'|      #
#    By: Jkutkut  https://github.com/jkutkut              /:::::::::::::\      #
#                                                        /:::::::::::::::\     #
#    Created: 2023/03/02 14:11:45 by Jkutkut            /:::===========:::\    #
#    Updated: 2023/03/07 10:34:08 by Jkutkut            '-----------------'    #
#                                                                              #
# **************************************************************************** #

import tkinter

from moneyconversor.style import ConversorStyle as STYLE

class Label(tkinter.Label):
    def __init__(self, window, text, font_size = STYLE.SUBTITLE_TEXT_SIZE):
        super().__init__(
            window,
            text = text,
            font = (STYLE.FONT, font_size),
            bg = STYLE.BG,
            fg = STYLE.FG
        )

class TitleLabel(Label):
    def __init__(self, window, text):
        super().__init__(window, text, STYLE.TITLE_TEXT_SIZE)

class SubTitleLabel(Label):
    def __init__(self, window, text):
        super().__init__(window, text, STYLE.SUBTITLE_TEXT_SIZE)

class NormalLabel(Label):
    def __init__(self, window, text):
        super().__init__(window, text, STYLE.NORMAL_TEXT_SIZE)

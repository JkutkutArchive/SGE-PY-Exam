# **************************************************************************** #
#                                                                              #
#                                                         .-------------.      #
#                                                         |.-----------.|      #
#                                                         ||           ||      #
#                                                         ||  Jkutkut  ||      #
#    app.py                                               ||           ||      #
#                                                         |'-----------'|      #
#    By: Jkutkut  https://github.com/jkutkut              /:::::::::::::\      #
#                                                        /:::::::::::::::\     #
#    Created: 2023/03/07 10:15:13 by Jkutkut            /:::===========:::\    #
#    Updated: 2023/03/07 10:15:16 by Jkutkut            '-----------------'    #
#                                                                              #
# **************************************************************************** #

from moneyconversor.gui import MoneyConversorGUI

class MoneyConversorApp:
    def __init__(self):
        self._gui = MoneyConversorGUI()
        self._init_logic()

    def _init_logic(self) -> None:
        pass # TODO 

    def run(self):
        self._gui.run()

    # def error(self, title, msg) -> None:
    #     messagebox.showerror(title = title, message = msg)



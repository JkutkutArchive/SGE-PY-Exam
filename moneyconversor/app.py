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
#    Updated: 2023/03/07 10:58:36 by Jkutkut            '-----------------'    #
#                                                                              #
# **************************************************************************** #

from tkinter import messagebox
from moneyconversor.gui import MoneyConversorGUI

class MoneyConversorApp:
    def __init__(self):
        self._gui = MoneyConversorGUI()
        self._init_logic()

    def _init_logic(self) -> None:
        self._gui.btn_submit.config(command = self._submmit)

    def _submmit(self) -> None:
        conversion_type = self._gui.conversion_type
        if conversion_type == None:
            self.error("Tipo conversión", "Selecciona un tipo de conversión.")
            return
        money = self.get_money()
        if not money:
            return
        fts = [
            lambda d: d * 0.947983,
            lambda e: e * 1.054883
        ]
        equivalent = fts[conversion_type](money)
        self._gui.convert(money, conversion_type, equivalent)

    def get_money(self) -> float | None:
        m = self._gui.money
        if m == '':
            self.error("Cantidad", "Introduce una cantidad de dinero válida")
            return None
        try:
            return float(m)
        except:
            self.error("Cantidad", "La cantidad no es válida (ej: 4.32)")
        return None

    def run(self):
        self._gui.run()

    def error(self, title, msg) -> None:
            messagebox.showerror(title = title, message = msg)



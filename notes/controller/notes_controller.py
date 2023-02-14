# Контроллер

from notes.services.user_interface import *

class NotesController:
    def __int__(self):
        self.menu_dict = {
            1:"добавить",
            2:"изменить",
            3:"удалить",
            4:"поиск",
            0:"выход"
        }

    def run(self):
        ui = UserIterface()

        menu = 1
        while menu != 0:
            menu = ui.show_menu(self.menu_dict)

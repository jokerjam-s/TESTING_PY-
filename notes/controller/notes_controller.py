# Контроллер
import services.*


class NotesController:
    menu_dict = {
        1:"добавить",
        2:"изменить",
        3:"удалить",
        4:"поиск",
        0:"выход"
    }

    def run(self):
        UserInterface
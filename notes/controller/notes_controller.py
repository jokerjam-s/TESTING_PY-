# Контроллер

from notes.views.node_view import *
from notes.models.notes_list import *


class NotesController:
    def __init__(self):
        self.menu_dict = {
            1:"добавить",
            2:"изменить",
            3:"удалить",
            4:"поиск",
            5:"загрузить",
            6:"сохранить",
            7:"показать все записи",
            0:"выход"
        }

        self.ui = UserIterface()
        self.view = NoteView()
        self.notes = NoteList()

    def run(self):
        menu = 1
        while menu != 0:
            menu = self.ui.show_menu(self.menu_dict)

            match menu:
                case 1:
                    self.append()
                case 2:
                    self.update()
                case 3:
                    self.delete()
                case 7:
                    self.show_all()


    # показать список задач
    def show_all(self):
        self.view.show_notes(self.notes.get_list())


    # поиск1
    #def find(self):



    # добавление
    def append(self):
        note = self.view.new_note();
        self.notes.add_note(note)


    # редактирование
    def update(self):
        note_no = self.ui.ask_int("Номер изменяемой записи: ")
        note = self.notes.get_note_no(note_no)
        if note == None:
            print("Запись не найдена!")
        else:
            self.view.edit_note(note)
            #self.notes.replace_note(old_note, note)
            print("Запись изменена!")


    # удаление
    def delete(self):
        note_no = self.ui.ask_int("Номер удаляемой записи: ")
        note = self.notes.get_note_no(note_no)
        if note != None:
            self.notes.del_note(note)
            print("Запись удалена!")
        else:
            print("Запись не найдена!")
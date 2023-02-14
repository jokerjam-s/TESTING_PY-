# Контроллер

from notes.views.node_view import *
from notes.models.notes_list import *
from notes.services.notes_to_from_json import NotesToTromJson

class NotesController:
    def __init__(self):
        self.menu_dict = {
            1:"добавить",
            2:"изменить",
            3:"удалить",
            4:"фильтр по тексту",
            5:"фильтр по дате",
            6:"загрузить",
            7:"сохранить",
            8:"показать все записи",
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
                case 4:
                    self.find_on_text()
                case 5:
                    self.find_on_date()
                case 6:
                    self.load_data()
                case 7:
                    self.save_data()
                case 8:
                    self.show_all()

    # сохранение списка задач в фал (сериализация)
    def save_data(self):
        json_service = NotesToTromJson()
        file_name = self.ui.ask_str("JSON файл для сохранения: ")
        json_service.notes_to_json(self.notes.get_list(), file_name)

    # чтение данных
    def load_data(self):
        json_service = NotesToTromJson()
        file_name = self.ui.ask_str("JSON файл для чтения: ")
        notes = json_service.notes_from_json(file_name)
        self.notes.set_list(notes)

    # показать список задач на дату
    def find_on_date(self):
        date = self.ui.ask_date("Дата заметок: ")
        notes = self.notes.find_on_date(date)
        self.view.show_notes(notes)


    # показать список всех задач
    def show_all(self):
        self.view.show_notes(self.notes.get_list())

    # поиск по тексту заметки
    def find_on_text(self):
        text = self.ui.ask_str("Текст заметки: ")
        notes = self.notes.find_on_text(text)
        self.view.show_notes(notes)

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
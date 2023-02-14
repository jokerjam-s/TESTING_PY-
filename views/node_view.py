# view

from notes.data.notes import Note
from notes.services.user_interface import *

class NoteView:

    def __int__(self):
        self.ui = UserIterface()

    # запрос новой заметки
    def new_note(self):
        note = Note()
        note.date_start = self.ui.ask_str("Дата: ")
        note.time_start = self.ui.ask_time("Время: ")
        note.text_note = self.ui.ask_str("Текст: ")

        return note

    # запрос номера записи для удаления
    def del_note(self):
        return self.ui.ask_int("Номер записи для удаления: ")

    # редактирование заметки
    def edit_note(self, note:Note):
        note.date_start = self.ui.ask_date("Дата (" + note.date_start + "):")
        note.time_start = self.ui.ask_time("Время (" + note.time_start + "): ")
        note.text_note = self.ui.ask_str("Новый текст: ")

        return note

    # отображение списка заметок
    def show_notes(self, notes:list):
        print("--------------------------------------------------------------")
        print("  #  |   дата   | время | текст ")
        print("--------------------------------------------------------------")
        for l in notes.sort(key=lambda n : n.date_start):
            print(f" {0:3} | {1} | {2} | {3}".format(l.note_no, l.date_start, l.time_start, l.text_note))

        print("--------------------------------------------------------------")
